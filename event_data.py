import mysql.connector as connector
from mysql.connector import errorcode
from faker import Faker

def connection_to_my_sql_server(connector):
    try:
        database_connection = connector.connect(
            user="root",
            host="localhost",
            password="Kunjara123@",
            database="dev-eventmart"
        )
        print("Connection Created Successfully")
        return database_connection
    except connector.Error as Err:
        return Err

connection_object = connection_to_my_sql_server(connector)

cursor = connection_object.cursor()

def insert_data_into_accesses(connection_object, cursor):
    insert_query = "INSERT INTO accesses (name, short_description, long_description) VALUES (%s, %s, %s)"
    values = [("Authentication","Authentication is the process of verifying the identity of a user, device, or system"," Authentication is used to ensure secure access to protected resources, typically involving the use of credentials, biometrics, or other verification methods. It plays a crucial role in safeguarding sensitive information and preventing unauthorized access to digital systems and data."),
               ("")
    ]
    try:
        cursor.execute(insert_query, values)
    except connection_object.connector.Error as e:
        print("MySQL Error: {0}".format(e))
    except Exception as e:
        return e

    connection_object.commit()

insert_data_into_accesses(connection_object, cursor)

connection_object.close()
cursor.close()

