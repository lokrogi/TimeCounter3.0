from MiniDBsetup import MiniDB
from datetime import datetime
blank = '==='


class Time(MiniDB):

    def start(self):
        now = datetime.now()
        today = now.strftime('%d.%m.%Y')
        now_time = now.strftime('%H:%M')

        if self.loadLastRow(1) == '===':
            self.save(today, now.hour, now.minute, blank, blank, blank, blank)
            return f'Start at: {now_time}.'
        else:
            return f"You've already started session."

    def end(self):
        now = datetime.now()
        today = now.strftime('%d.%m.%Y')
        now_time = now.strftime('%H:%M')

        if self.loadLastRow(1) != '===':

            s_h = int(self.load(1))
            s_m = int(self.load(2))

            if s_m > now.minute:
                delta_h = (now.hour - 1) - s_h
                delta_min = (now.minute + 60) - s_m

            elif s_m <= now.minute:
                delta_h = now.hour - s_h
                delta_min = now.minute - s_m

            sum_hour = delta_h + int(self.load(5))
            sum_min = delta_min + int(self.load(6))
            if sum_min >= 60:
                sum_min -= 60
                sum_hour += 1

            self.save(today, blank, blank, delta_h, delta_min, sum_hour, sum_min)
            return f"End at: {now_time}.\n" \
                   f"Today's session time: {delta_h}h, {delta_min}min."

        else:
            return f"You've already finished the session"

    def showTotalTime(self):
        sum_hour = self.load(5)
        sum_min = self.load(6)
        return f'Time in total: {sum_hour}h, {sum_min}min'

    def show3lastSessions(self):
        list_h = self.loadSessions(3)
        list_min = self.loadSessions(4)
        list_date = self.loadSessions(0)

        return f'Date is in form: (day.month.year).\n' \
               f' \n' \
               f'III session: ({list_date[2]}) - {list_h[2]}h,{list_min[2]}min.\n' \
               f'II session: ({list_date[1]}) - {list_h[1]}h,{list_min[1]}min.\n' \
               f'Last session: ({list_date[0]}) - {list_h[0]}h,{list_min[0]}min. '
