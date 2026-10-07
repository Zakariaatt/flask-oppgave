import mariadb

def hentedata():
    try:
        with mariadb.connect(
            user="zakaria",
            password="1234",
            host="localhost",
            port=3306,
            database="flaskeDB"
        ) as conn:

            mycursor = conn.cursor()

            mycursor.execute("SELECT * FROM flasketyper")

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

            return myresult

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
