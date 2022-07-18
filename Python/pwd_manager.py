import sqlite3


try:
    con = sqlite3.connect('pwd.db')
    cur = con.cursor()
except Exception as err:
    print(err)

cur.execute('''CREATE TABLE  IF NOT EXISTS login_data
               (acount text, 
               user_name text, 
               password text)''')

account_name = input('Account: ')
user_name = input('User Name: ')
pwd_account = input('Password: ')

cur.execute("INSERT INTO login_data VALUES (?, ?, ?)", (account_name, user_name, pwd_account))

for row in cur.execute('SELECT * FROM login_data'):
        print(row)

con.commit()
con.close()