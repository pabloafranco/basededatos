import pymysql
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id  INT UNSIGNED AUTO_INCREMENT  PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

users = [
    ("user1", "password", "user1.gmail.com"),
    ("user2", "password", "user2.gmail.com"),
    ("user3", "password", "user3.gmail.com"),
    ("user4", "password", "user4.gmail.com"),
    ("user5", "password", "user5.gmail.com"),
]

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(host='localhost', 
                                  port=3306, 
                                  user=config('USER_MYSQL'), 
                                  passwd=config('PASWORD_MYSQL'), 
                                  db=config('DB_MYSQL'))

        # cursor = connect.cursor()
        # Esta opcion cierra solo la conexion, esto es un contexto
        with connect.cursor() as cursor:
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)


            query =  "INSERT INTO users ( username, password, email )  VALUES (%s, %s, %s)"
            #values = ("eduardo_gpg", "123", "eduardo@codigofacilito.com")

            #cursor.execute(query, values)
            #connect.commit()

            #for user in users:
            #    cursor.execute(query, user)

            cursor.executemany(query, users)
            connect.commit()

            query = "SELECT * from USERS"
            #query = "SELECT * from USERS LIMIT 3"
            rows = cursor.execute(query)

            #print (rows)
            #for users in cursor.fetchall():
            #for users in cursor.fetchmany(2):
            #    print (users)
            user = cursor.fetchone()
            print (user)

        #print ('Conexion realizad en forma exitosa')

    except pymysql.err.OperationalError as err:
        print ('No fue posible conectarse a la base de datos');
        print (err)

    finally:
        
        connect.close

        print ('Conexion finalizada de forma exitosa')
