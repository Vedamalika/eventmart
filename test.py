import pandas as pd
import mysql.connector as connector
from sqlalchemy import create_engine

# engine = create_engine("mysql+mysqlconnector://eventmart-user:'eC@2y@*gx1p0'@146.190.8.44:3306/dev-eventmart")
# engine = create_engine("mysql+mysqlconnector://eventmart-user:eC%402y%40%2Agx1p0@146.190.8.44:3306/dev-eventmart")
engine = create_engine("mysql+mysqlconnector://root:Kunjara123%40@localhost:3306/dev-eventmart")


def countries_data_inserting():
    try:
        countries_table_required_columns = ["id","name","phone_code","currency","region","sub_region","time_zone"]
        countries_df = pd.read_csv('countries_modified_data_two.csv',usecols=countries_table_required_columns)
        countries_df.to_sql('countries', engine, if_exists='append', index=False)
        print("In countries table data data_inserted successfully")
    except Exception as Err:
        print(Err)


def states_data_inserting():
    try:
        states_table_required_columns = ["id","name","country_id"]
        states_df = pd.read_csv('states_modified_data.csv',usecols=states_table_required_columns)
        states_df.to_sql('states', engine, if_exists='append', index=False)
        print("In states table data inserted successfully")
    except Exception as Err:
        print(Err)


def cities_data_inserting():
    try:
        cities_table_required_columns = ["id",'name','state_id','latitude','longitude']
        states_df = pd.read_csv('cities_modified_data_two.csv',usecols=cities_table_required_columns)
        states_df.to_sql('cities', engine, if_exists='append', index=False)
        print("In cities table data inserted successfully")
    except connector.IntegrityError as integrity_error:
        #it is occurred because of when avoids foreign key
        print(f'Integrity Error occurred: {integrity_error}')
    except connector.ProgrammingError as programming_error:
        #it is comes when syntax SQl syntax such when we try to inserting data into non existing tables
        print(f'Programming Error occurred: {programming_error}')
        #it raises improper connection to mysql server
    except connector.OperationalError as operation_error:
        print(f'Operational Error Occurred: {operation_error}')
        #it happens when mysql server problem is occurred
    except connector.DataError as data_error:
        print(f'Data Error is: {data_error}')

# countries_data_inserting()
# states_data_inserting()
cities_data_inserting()

