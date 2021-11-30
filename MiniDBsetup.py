import csv


class MiniDB:
    def save(self, date, s_hour, s_minute, session_h, session_m, sum_hour, sum_min):
        to_save = [date, s_hour, s_minute, session_h, session_m, sum_hour, sum_min]
        with open('TimeDB.csv', 'a') as db_csv:
            db_reader = csv.writer(db_csv, delimiter=';')
            db_reader.writerow(to_save)

        db_csv.close()

    # Date=0  s_hour=1  s_minute=2  session_h=3  session_m=4  sum_hour=5  sum_min=6
    def load(self, col_index):
        with open('TimeDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            x = -2
            while rows[x][col_index] == '===':
                x -= 2
            else:
                return rows[x][col_index]

    def load_last_row(self, col_index):
        with open('TimeDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            return rows[-2][col_index]

    def load_sessions(self, col_index):
        with open('TimeDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            sessions = []
            x = -2
            while len(sessions) < 3:
                while rows[x][4] == '===':
                    x -= 2
                else:
                    sessions.append(rows[x][col_index])
                    x -= 2
            return sessions

    def clear_db(self):
        with open('TimeDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            if len(rows) > 50:
                # clearing blank rows (lists) in db
                try:
                    y = 1
                    for x in rows:
                        rows.pop(y)
                        y += 1
                except IndexError:
                    pass

                # clearing first 19 rows (lists)
                z = 0
                while z <= 19:
                    rows.pop(0)
                    z += 1
                # saving
                with open('TimeDB.csv', 'w') as db_file:
                    db_clear = csv.writer(db_file, delimiter=';')
                    for x in rows:
                        db_clear.writerow(x)

        db_csv.close()
