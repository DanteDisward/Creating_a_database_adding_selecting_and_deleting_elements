import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
DROP TABLE Users
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
        (f"User{i}", f"example{i}@gmail.com", f"{i}0"))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 > 0")

cursor.execute("SELECT COUNT(*) FROM Users")

i = 1
c = cursor.fetchall()[0][0]
while i <= c:
    if i <= c:
        cursor.execute(f"DELETE FROM Users WHERE id = {i}")
        i += 3

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
for i in cursor.fetchall():
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

connection.commit()
connection.close()
