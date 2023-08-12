
import mysql.connector as connector
from mysql.connector import errorcode
from faker import Faker
# from sql_querys import query_list
import random
random_boolean = [1,0,1,1,0]
random_boolean_for_offering = [0,1,0,1,1,0,1,0,1,1,0,1,0,1,1]
random_boolean_for_users = [1,0,1,1,0,1,0,1,1,0,1,0,1,1,0]
faker = Faker()
from test import countries_data_inserting
from test import states_data_inserting
from test import cities_data_inserting
def connection_to_my_sql_server(connector):
    try:
        database_connection = connector.connect(
            user = "root",
            host = "localhost",
            password = "Kunjara123@",
            database = "dev-eventmart"
        )
        print("Connection Created Successfully")
        return database_connection
    except connector.Error as Err:
        return Err
connection_object = connection_to_my_sql_server(connector)

cursor = connection_object.cursor(connector)
# def creating_database(cursor,query):
#     try:
#         database = cursor.execute(query)
#         print("Database Created Successfully")
#         return database
#     except connector.Error as Err:
#         return Err
# creating_data_base_query = "CREATE DATABASE air_port_data"
# database = creating_database(cursor,creating_data_base_query)

access_query = "INSERT INTO accesses (name,short_description,long_description) VALUES(%s,%s,%s)"   
countries_query = "INSERT INTO countries (name,phone_code,currency,region,sub_region,time_zone) VALUES(%s,%s,%s,%s,%s,%s)"
states_query  = "INSERT INTO states (name,country_id) VALUES(%s,%s)"
cities_query = "INSERT INTO cities (name,state_id,latitude,longitude) VALUES(%s,%s,%s,%s)"
organization_query = """INSERT INTO organization(name,phone_number_1,phone_number_2,email_1,email_2,address_line_1,address_line_2,gst_number,city_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
role_query = "INSERT INTO roles(name)VALUES(%s);"
roles_access = "INSERT INTO roles_accesses(role_id,access_id,full_access,is_web,is_mobile)VALUES(%s,%s,%s,%s,%s);"
users_query = "INSERT INTO users(first_name,last_name,phone_number,whatsapp_number,email,role_id,date_of_birth,profile_pic_id,is_employee) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
employees_query = """INSERT INTO employees(pan_number,emp_id,users_id,address_line_1,address_line_2,city_id,pincode)VALUES(%s,%s,%s,%s,%s,%s,%s);"""
vendors_query = """INSERT INTO vendors(name,pan_number,gst_number,terms_and_conditions,user_id,short_description,long_description,address_line_1,address_line_2,city_id,pincode,facebook_link,instagram_link,youtube_link) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

customers_query = """INSERT INTO customers(name,is_businesscustomer,pan_number,gst_number,user_id,adhaar_number)VALUES(%s,%s,%s,%s,%s,%s);"""

customers_address_query = """INSERT INTO customer_addresses(address_line_1,address_line_2,pincode,customer_id,phone_number,city_id)VALUES(%s,%s,%s,%s,%s,%s);"""
branches_query = """INSERT INTO branches(name,phone_number,organization_id,email_id,address_line_1,address_line_2,city_id,pincode)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
event_manager_event_query = """INSERT INTO eventmanager_event(employee_id,start_time,end_time,customer_id)VALUES(%s,%s,%s,%s);"""
add_on_category_query = """INSERT INTO add_on_categories(name,short_description,long_description)VALUES(%s,%s,%s)"""
add_ons_query = """INSERT INTO add_ons(name,short_description,long_description,file_id,offerings_id,price)VALUES(%s,%s,%s,%s,%s,%s);"""
add_on_category_add_ons_query = """INSERT INTO add_on_category_add_ons(add_on_categories_id,add_ons_id)VALUES(%s,%s)"""
unit_of_measurement_table_query = """INSERT INTO unit_of_measurements(name,abbreviation)VALUES(%s,%s);"""
gst_table_query = """INSERT INTO gst(percentage)VALUES(%s);"""
cart_query = """INSERT INTO carts(cart_status_id,customer_id)VALUES(%s,%s)"""
coupons_query = """INSERT INTO coupons(name,coupon_code,expiry_date,coupon_type,min,max,description)VALUES(%s,%s,%s,%s,%s,%s,%s);"""
orders_query = """INSERT INTO orders(coupon_id,total_cost,gst,discount,coupon_discount,delivery_date,delivery_charges,delivery_address,opt_eventmanager,eventmanger_cost,customer_id)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
statuses_of_orders_query = """INSERT INTO statuses_of_orders(orders_id,statuses_id,short_description,long_description)VALUES(%s,%s,%s,%s)"""
order_status_query = """INSERT INTO order_statuses(status_code,name,description,remarks,customer_status,customer_status_name)VALUES(%s,%s,%s,%s,%s,%s)"""
invoice_query = """INSERT INTO invoices(invoice_number,short_description,long_description,orders_id,payment_status)VALUES(%s,%s,%s,%s,%s)"""
biddings_query = """INSERT INTO biddings(from_vendor,expiry_date,order_id,is_active,is_otp_valid,remarks)VALUES(%s,%s,%s,%s,%s,%s);"""
event_categories_query = """INSERT INTO event_categories(name,short_description,long_description,files_id)VALUES(%s,%s,%s,%s)"""
event_category_offerings = """INSERT INTO event_category_offerings(event_categories_id,offerings_id)VALUES(%s,%s);"""
wish_list = """INSERT INTO wishlists(offerings_id,customers_id)VALUES(%s,%s);"""
employees_branches_query = """INSERT INTO employees_branches(employees_id,branches_id)VALUES(%s,%s);"""
files_query = """INSERT INTO files(name,file_type,file_size,file_path,short_description,long_description) VALUES(%s,%s,%s,%s,%s,%s);"""
offering_files = """INSERT INTO offering_files(offering_ids,file_ids)VALUES(%s,%s);"""
offering_category = """INSERT INTO offering_categories(name,short_description,long_description,files_id)VALUES(%s,%s,%s,%s);"""
offering_sub_category = """INSERT INTO offering_sub_categories(name,short_description,long_description,offering_category_id,files_id)VALUES(%s,%s,%s,%s,%s);"""
order_add_ons = """INSERT INTO order_add_ons(orders_id,add_ons_id,quantity)VALUES(%s,%s,%s)"""
orders_items_query = """INSERT INTO orders_items(order_id,offering_id,quatity)VALUES(%s,%s,%s);"""
vendors_files = """INSERT INTO vendors_files
(vendor_ids,
file_ids)
VALUES
(%s,%s);"""
cart_statuses_query = """
INSERT INTO cart_statuses
(
name,
short_description,
long_description)
VALUES
(%s,%s,%s)"""
offering_sub_category
offerings_query = """INSERT INTO offerings 
(name,short_description,long_description,cgst,sgst,igst,actual_price,discount_price,
is_product,is_service,unit_of_measurement_id,base_quantity,offering_sub_categories_id,vendor_id,sku,hsn_code,sac_code,in_stock,tags) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
cart_items_query = """INSERT INTO cart_items
(
cart_id,
offerings_id,
quantity)
VALUES
(%s,%s,%s)"""
confirmed_orders_query = """INSERT INTO confirmed_orders(order_id,active_status)VALUES(%s,%s)"""



def deleting_rows(table):
    try:
        delete_query = f"DELETE FROM {table}"
        cursor.execute(delete_query)
        connection_object.commit()
        print(f'{table} table rows deleted successfully....')
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
        
        
deleting_rows("accesses")
deleting_rows("add_on_categories")
deleting_rows("add_on_category_add_ons")
deleting_rows("add_ons")
deleting_rows("biddings")
deleting_rows("branches")
deleting_rows("cart_items")
deleting_rows("carts")
deleting_rows("cart_statuses")
deleting_rows("orders_items")
deleting_rows("offerings")
deleting_rows("vendors")
deleting_rows("orders")
deleting_rows("customer_adresses")
deleting_rows("cities")
deleting_rows("customers")
deleting_rows("users")
deleting_rows("offering_sub_categories")
deleting_rows("offering_categories")
deleting_rows("files")
deleting_rows("roles")
deleting_rows("states")
deleting_rows("countries")
deleting_rows("coupons")
deleting_rows("employees")
deleting_rows("employees_branches")
deleting_rows("event_categories")
deleting_rows("event_category_offerings")
deleting_rows("eventmanager_event")
deleting_rows("gst")
deleting_rows("invoices")
deleting_rows("offering_categories")
deleting_rows("offering_files")
deleting_rows("offerings")
deleting_rows("order_add_ons")
deleting_rows("order_statuses")
deleting_rows("organization")
deleting_rows("roles")
deleting_rows("roles_accesses")
deleting_rows("states")
deleting_rows("statuses_of_orders")
deleting_rows("confirmed_orders")
deleting_rows("unit_of_measurements")
deleting_rows("users")
deleting_rows("vendors_files")
deleting_rows("wishlists")
deleting_rows("cart_items")



def drop_event_mart_db(drop_query = "DROP DATABASE eventmart;"):
    try:
        cursor.execute(drop_query)
        print("DB deleted_successfully")
        connection_object.commit()
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
# drop_event_mart_db()
    

query_list = [access_query,
              add_on_category_query,
              files_query,
              gst_table_query,
              offering_category,
              offering_sub_category,
              countries_query,
              states_query,
              cities_query,
              role_query,
              users_query,
              vendors_query,
              unit_of_measurement_table_query,
              offerings_query,
              add_ons_query,
              add_on_category_add_ons_query,
              cart_statuses_query,
              customers_query,
              cart_query,
              
              customers_address_query,
              coupons_query,
              orders_query,
              biddings_query,
              organization_query,
              branches_query,
              employees_query,
              employees_branches_query,
              event_categories_query,
              event_category_offerings,
              event_manager_event_query,
              invoice_query,
              offering_files,
              order_add_ons,
              orders_items_query,
              order_status_query,
              statuses_of_orders_query,
              confirmed_orders_query,
              roles_access,
              vendors_files,
              wish_list,
              cart_items_query
              ]
access_query
def inserting_data_into_tables():  # sourcery skip: avoid-builtin-shadow, convert-to-enumerate, for-index-underscore, hoist-statement-from-loop, switch
    try:
        no_of_query_counter = 1
        for i in query_list:
        # organization
            if i == organization_query:
                data_4 = ("Eventmart",9979855458,8979855458,faker.email(),faker.email(),faker.address()[:42],faker.address()[:42],"07AAGFF2194N1Z7",1)
                cursor.execute(i,data_4)
                connection_object.commit()
        #access_query
            if i == access_query:
                index_5 = 1
                for k in range(0,5):
                    print('inserting data into access_query table....')
                    access_names = ["Authentication","Add User","User Management","Product Listing","View"]
                    access_query_description = ["Authentication is the process of verifying the identity of a user or entity, ensuring secure access to information or resources.",
                                         "Adding a user involves creating a new account, granting permissions and access rights in a system or application.",
                                         "User management involves overseeing user accounts, permissions, and access, ensuring efficient administration and security in a system.",
                                         "Product listing entails creating a catalog of products with details, descriptions, and specifications for effective presentation and sales.",
                                         "View allows users to visually access and examine information or content, offering a convenient and concise way to consume data or media."
                                        ]
                    data_5 = (access_names[k],access_query_description[k][:150],access_query_description[k])
                    cursor.execute(i,data_5)
                    connection_object.commit()
                    index_5 +=1
            # add_on_categories
            if(i == add_on_category_query):
                        add_on_category_table_id = 1
                        add_on_category_names = ["Photography","Music","Food","Drink","Decoration"]
                        add_on_category_table_short_description = ["Preserve unforgettable occasions with our exceptional camera. From weddings to birthdays, seize the essence of special moments",
                                                                   "Music sets the perfect ambiance for every occasion. From weddings and parties to graduations and ceremonies, it creates an atmosphere of joy and celebration.",
                                                                   "Satisfy your cravings with our delicious food! From tasty appetizers to mouthwatering main courses and irresistible desserts, we've got something for everyone.",
                                                                   "Quench your thirst with our refreshing drink selection! From icy cold beverages to aromatic hot drinks, we have a variety of options to satisfy your cravings.",
                                                                   "Transform your space into a captivating wonderland with our exquisite decorations."]
                        
                        add_on_category_table_long_description = [
                            "Our cameras boast high-resolution sensors, intuitive controls, and advanced features to ensure that you never miss a shot.",
                            "With our curated playlists and extensive music library, you can create the perfect soundtrack for your day. Whether you're looking to relax, dance, or simply enjoy the melodies, our music will transport you to a world of sonic bliss.",
                            "Our talented chefs carefully craft each dish using the freshest ingredients and flavors that will leave you craving for more. Whether you're in the mood for comfort food or exploring adventurous flavors, our diverse menu has something to please every palate.",
                            "Our drinks are crafted with care, using high-quality ingredients to ensure a flavorful and satisfying experience. Join us and raise a glass to delicious refreshment",
                            "Our decorations range from chic and minimalist to vibrant and festive, catering to various themes and preferences."
                        ]
                        for k in range(0,5):
                            print('inserting data into add_on_categories table....')
                            add_on_category_table_data = (add_on_category_names[k],add_on_category_table_short_description[k][:150],add_on_category_table_long_description[k])
                            cursor.execute(i,add_on_category_table_data)
                            connection_object.commit()
                            add_on_category_table_id +=1
            # files_query     
            if i == files_query:
                files_table_id = 1
                file_names = ["file.jpg","file.text","file.pdf","file.xls","file.csv"]
                file_types = ["jpg","text","pdf","xls","csv"]
                file_size = [100,200,300,100,55]
                file_path = ["Desktop/folder_one","Desktop/folder_two","Desktop/folder_three","Desktop/folder_four","Desktop/folder_five"]
                files_table_description = ["Capture and preserve your memories with this JPEG image file. It's perfect for storing and sharing your favorite photos, ensuring they stay vivid and accessible for years to come.",
                                           "Easily view and edit this plain text file. Whether it's a note, a document, or a simple message, this file format provides a straightforward and versatile way to store and manage textual information.",
                                           "Open this PDF file to access professional documents, reports, or e-books. PDFs maintain formatting integrity across different devices, making it easy to view, print, and share content while retaining its original layout.",
                                           "Unlock the power of data with this Excel spreadsheet file. Organize, analyze, and calculate numerical information effortlessly. Excel provides a range of tools and functions to help you make sense of your data, from simple tables to complex formulas and charts.",
                                           "Dive into data analysis with this CSV (Comma-Separated Values) file. CSV format allows for easy exchange and manipulation of tabular data, making it suitable for tasks like importing data into databases or performing statistical analysis."
                                        ]
                for k in range(0,5):
                    print('inserting data into files table....')
                    files_table_data = (file_names[k],file_types[k],file_size[k],file_path[k],files_table_description[k][:45],files_table_description[k])
                    cursor.execute(i,files_table_data)
                    connection_object.commit()
                    files_table_id +=1
                    
            # gst Table
            if(i == gst_table_query):
                index_37  = 1
                gst_percentages = [5,12,18,28,30]
                for k in range(0,5):
                    print('inserting data into gst table....')
                    data_11 = ([gst_percentages[k]])
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    index_37 +=1        
                    
            # offering_category 
            if i == offering_category:
                offering_category_table_id = 1
                file_id = 5
                offering_category_names = ["Photography","Music","Food","Drink","Decoration"]
                offering_category_table_short_description = ["Unforgettable occasions with our exceptional camera. From weddings to birthdays, seize the essence of special moments",
                                                                   "Sets the perfect ambiance for every occasion. From weddings and parties to graduations and ceremonies, it creates an atmosphere of joy and celebration.",
                                                                   "Satisfy your cravings with our delicious food! From tasty appetizers to mouthwatering main courses and irresistible desserts, we've got something for everyone.",
                                                                   "Quench your thirst with our refreshing drink selection! From icy cold beverages to aromatic hot drinks, we have a variety of options to satisfy your cravings.",
                                                                   "Transform your space into a captivating wonderland with our exquisite decorations."]
                for k in range(0,5):
                    print('inserting data into offering_category table....')
                    data_11 = (offering_category_names[k],offering_category_table_short_description[k][:150],offering_category_table_short_description[k],file_id)
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    offering_category_table_id +=1
                    file_id -= 1


                # offering_sub_category_table
            if(i == offering_sub_category):
                files_id_list = [1,2,2,3,3,4,5,5,5,2]
                offering_sub_category_table_id = 1
                offering_id_list = [1,1,2,2,3,3,4,4,5,5]
                offering_sub_category_name = ["Indore Shoot","Out Door Shot","Sangeeth DJ","Sound Systems","Veg","Non-veg","Alcohol","Non-alcohol","Lighting","Flowers Decoration"]
                offering_sub_category_table_description = [
                    "Capture your dream wedding in Indore, where tradition meets elegance. Cherish every moment amidst stunning venues, rich cultural heritage, and delectable cuisine.",
                    "Embark on an extraordinary outdoor shoot in Indore, where nature becomes your canvas. Discover breathtaking landscapes, from lush green parks to serene lakes, offering a stunning backdrop for your creative vision.",

                    "Experience the magic of a Sangeet ceremony in Indore, where music and celebration intertwine. Immerse yourself in the rhythmic beats and melodic tunes as you dance and sing your heart out.",
                    "Indulge in an unparalleled audio experience with top-notch sound systems in Indore. Whether it's a live concert, corporate event, or private function, Indore offers state-of-the-art sound systems to elevate your auditory journey.",
                    
                    "Indulge in the flavors of vegetarian cuisine in Indore, a paradise for veggie lovers. Discover a tantalizing array of delectable vegetarian dishes that showcase the city's rich culinary heritage.",
                    "Savor the diverse and flavorsome non-vegetarian cuisine in Indore, a paradise for meat enthusiasts. Indulge in a wide range of delectable dishes that showcase the city's culinary prowess.",
                    
                    "Indulge in the vibrant nightlife of Indore, where you can enjoy a wide variety of alcoholic beverages.",
                    "Experience the refreshing world of non-alcoholic beverages in Indore, where a delightful range of options awaits.",
                    
                    "Illuminate your world with mesmerizing lighting options in Indore. Whether it's for a special event, photography, or ambiance enhancement, Indore offers a wide range of lighting solutions to transform any space.",
                    "Immerse yourself in the beauty and fragrance of flower decoration in Indore. "
                ]
                for k in range(0,10):
                    print('inserting data into offering_sub_category_table table....')
                    offering_sub_category_table_data = (offering_sub_category_name[k][:45],offering_sub_category_table_description[k][:150],offering_sub_category_table_description[k],offering_id_list[k],files_id_list[k])
                    cursor.execute(i,offering_sub_category_table_data)
                    connection_object.commit()
                    offering_sub_category_table_id +=1
                    
                    
            # countries
            if i == countries_query:
                countries_data_inserting()
                    
            # states_query
            if i == states_query:
                states_data_inserting()
                    
        #cities_query
            if i == cities_query:
                cities_data_inserting()        
                    
                    
        #role_query
            if i == role_query:
                index_6 = 1
                roles_name = ["Admin","Customer","Event Manager","Sales Manager","Vendor"]
                for k in range(0,5):
                    print('inserting data into roles table....')
                    data_6 = (([roles_name[k]]))
                    cursor.execute(i,data_6)
                    connection_object.commit()
                    index_6 +=1
                    
        # roles_access
            if i == roles_access:
                index_7 = 1
                index_8 = 5
                for k in range(0,5):
                    print('inserting data into roles_access  table....')
                    data_7 = (index_7,index_8,random_boolean[k],random_boolean[k],random_boolean[k])
                    cursor.execute(i,data_7)
                    connection_object.commit()
                    index_7 += 1
                    index_8 -= 1
        
        # # users_table
            if i == users_query:
                index_10 = 1
                roles=1
                primary=1
                boolean_index = 0
                phone_numbers = [9979855458,8744541775,7478548789,7545487561,7587121548,9979855458,8979855458,7744541775,7478548789,6545487561,8587121548,8744541775,7478548789,7545487561,7587121548]
                phone_numbers_two = [8979855458,7744541775,7478548789,6545487561,8587121548,9979855458,8744541775,7478548789,7545487561,7587121548,9979855458,8979855458,7744541775,7478548789,6545487561,8587121548,9979855458]
                for k in range(0,15):
                    print('inserting data into users table....')
                    data_9 = (faker.first_name(),faker.last_name(),phone_numbers[k],phone_numbers_two[k],faker.email(),roles,faker.date(),index_10,random_boolean_for_users[k])
                    # data_8 = (index_9,faker.name(),file_names[k],file_types[k],file_size[k],faker.text()[:45],faker.text())
                    cursor.execute(i,data_9)
                    connection_object.commit()
                    index_10 +=1
                    primary +=1
                    if index_10>5:
                        index_10=1
                    if k<4:
                        roles =1
                    elif k>=4 and k<9:
                        roles=2
                    else:
                        roles=5
                    boolean_index +=1
        #employees
            if i == employees_query:
                index_11 = 1
                pan_numbers = ["BZSPN9TP","BYSPN8UP","BZSPN747NP","BZSPN7NO","BZSPN5NM"]
                employee_id = ['89798554581212','7744541775','74785487898787','654548756174455','85878781']
                pincodes = [523310,523318,523318,526698,523301]
                for k in range(0,5):
                    print('inserting data into employees table....')
                    data_9 = (pan_numbers[k],employee_id[k],index_11,faker.street_address()[:45],faker.street_name(),index_11,pincodes[k])
                    # data_8 = (index_9,faker.name(),file_names[k],file_types[k],file_size[k],faker.text()[:45],faker.text())
                    cursor.execute(i,data_9)
                    connection_object.commit()
                    index_11 +=1

            #vendors_table
            if i == vendors_query:
                index_12 = 1
                vendor_role=10
                pan_numbers = ["BZSPN9TP","BYSPN8UP","BZSPN747NP","BZSPN7NO","BZSPN5NM"]
                gst_numbers = ["07AAGFF794N1Z1","07AAGFF2294N1Z1","07AAGFF2194N1Z8","07AAGFF2194N1Z7","07AAGFF2194N1Z2"]
                pincodes = [523310,523318,523318,526698,523301]
                for k in range(0,5):
                    print('inserting data into vendors table....')
                    data_9 = (faker.name(),pan_numbers[k],gst_numbers[k],faker.text(),vendor_role,faker.text()[:15],faker.text(),faker.street_address(),faker.street_name(),index_12,pincodes[k],faker.url(),faker.url(),faker.url())
                    cursor.execute(i,data_9)
                    connection_object.commit()
                    index_12 +=1
                    vendor_role+=1

            # cart_statuses Table
            if i == cart_statuses_query:
                # print(i)
                index_13 = 1
                cart_status_names = ["Active","Pending","In Review","On Hold","Completed"]
                cart_statuses_short_description = ["The item(s) in your cart are awaiting processing. Please wait for confirmation or further instructions.",
                                                   "Your cart is active and ready for checkout. Proceed to payment to complete your purchase.",
                                                   "The contents of your cart are currently under review. Our team is assessing the details and will provide feedback or recommendations.",
                                                   "Your cart is temporarily on hold. This may be due to stock availability or other factors. We will notify you once it is resolved.",
                                                   "Congratulations! Your cart has been successfully processed and your order is complete. Sit back and await your delivery."
                                                   ]
                cart_statuses_long_description = ["The item(s) in your cart are currently in a pending status, awaiting further processing. This could be due to various reasons, such as verification of payment, availability of stock, or order confirmation.",
                                                  "Congratulations! Your cart is active and ready for checkout. You have selected the desired items, and now it's time to proceed to the payment stage. You can review the contents of your cart, make any necessary adjustments, and proceed to the secure payment process.",
                                                  "Your cart is currently in the review stage, where our team carefully examines the details of your order. This process involves verifying the accuracy of the items, quantities, and any customization options you may have selected.",
                                                  " We regret to inform you that your cart is currently on hold. This status indicates that there may be a temporary delay or issue that needs attention before we can proceed with processing your order. This could be due to various reasons, such as stock availability, payment verification, or shipping restrictions.",
                                                  "Congratulations! Your cart has been successfully processed, and your order is now complete. We would like to express our sincere gratitude for choosing our products and entrusting us with your purchase."
                                                  ]
                for k in range(0,5):
                    print('inserting data into cart_status table....')
                    data_10 = (cart_status_names[k],cart_statuses_short_description[k][:45],cart_statuses_long_description[k][:150])
                    cursor.execute(i,data_10)
                    connection_object.commit()
                    index_13 +=1
            
            
                    
                    
            # cart Table
            if i == cart_query:
                cart_table_id = 1
                cart_statuses_id_list = [1,1,2,5,5]
                customer_id = 1
                for k in range(0,5):
                    print('inserting data into cart table....')
                    data_11 = (cart_statuses_id_list[k],customer_id)
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    cart_table_id +=1
                    customer_id +=1
            # customer
            if i == customers_query:
                # print(query_list[i])
                customers_table_id = 1
                user_id = 6
                adhaar_number = [67979855458,68744541775,67478548789,37545487561,57587121548]
                pan_numbers = ["BZSPN9TP","BYSPN8UP","BZSPN747NP","BZSPN7NO","BZSPN5NM"]
                gst_numbers = ["07AAGFF794N1Z1","07AAGFF2294N1Z1","07AAGFF2194N1Z8","07AAGFF2194N1Z7","07AAGFF2194N1Z2"]
                customers_names = ["Aiden","","Liam","Noah",""]
                for k in range(0,5):
                    print('inserting data into customers_query table....')
                    customers_table_data = (customers_names[k],random_boolean[k],pan_numbers[k],gst_numbers[k],user_id,adhaar_number[k])
                    cursor.execute(i,customers_table_data)
                    connection_object.commit()
                    customers_table_id +=1
                    user_id +=1
                    

            #Customer_Adresses
            if (i == customers_address_query):
                # print(query_list[i])
                customers_address_table_id = 1
                customer_id_list = [1,1,3,4,4]
                city_id = 1
                phone_number = [9979855458,8744541775,7478548789,7545487561,7587121548]
                pincodes = [523310,523318,523318,526698,523301]
                gst_numbers = ["07AAGFF794N1Z1","07AAGFF2294N1Z1","07AAGFF2194N1Z8","07AAGFF2194N1Z7","07AAGFF2194N1Z2"]
                for k in range(0,5):
                    print('inserting data into Customer_Addresses table....')
                    customers_address_data = (faker.street_address() ,faker.street_name(),
                    pincodes[k],customer_id_list[k],
                    phone_number[k],city_id)
                    cursor.execute(i,customers_address_data)
                    connection_object.commit()
                    customers_address_table_id  +=1
                    city_id +=1
            # branches
            if (i == branches_query):
                # print(query_list[i])
                branches_table_id = 1
                city_id = [1,1,1,2,2]
                phone_number = [9979855458,8744541775,7478548789,7545487561,7587121548]
                pincodes = [523310,523318,523318,526698,523301]
                gst_numbers = ["07AAGFF794N1Z1","07AAGFF2294N1Z1","07AAGFF2194N1Z8","07AAGFF2194N1Z7","07AAGFF2194N1Z2"]
                for k in range(0,5):
                    print('inserting data into branches table....')
                    data_11 = (
                        
                        f"{faker.name()} PVT.LTD",
                        phone_number[k],
                        1,
                        faker.email(),
                        faker.street_address()[:45],
                        faker.street_name(),
                        city_id[k],
                        pincodes[k],
                    )

                    cursor.execute(i,data_11)
                    connection_object.commit()
                    branches_table_id +=1
                    
                    
            # employee_branches Table
            if (i == employees_branches_query):
                employees_branches_table_id = 1
                branches_id = 1
                for k in range(0,5):
                    print('inserting data into employee_branches_table....')
                    employee_branches_table_data = (employees_branches_table_id, branches_id)
                    cursor.execute(i,employee_branches_table_data)
                    connection_object.commit()
                    employees_branches_table_id +=1
                    branches_id +=1
                        
                # event_manager_event Table
            if(i == event_manager_event_query):
                    # print(query_list[i])
                event_manager_event_table_id = 1
                employee_id  = 5
                customer_id = event_manager_event_table_id
                for k in range(0,5):
                    print('inserting data into event_manager_event table....')
                    data_11 = (employee_id,faker.future_datetime(),faker.future_datetime(),customer_id)
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    event_manager_event_table_id +=1
                    employee_id -=1
                    customer_id +=1
                
                
                
                
                # unit_off_meassurements table
            if(i == unit_of_measurement_table_query):
                # print(query_list[i])
                unit_of_measurement_table_id = 1
                names = ["Meter","Milli Litres","Centimeter","Gram","Inch"]
                abbreviation = ["M","ML","CM","GM","INC"]
                
                for k in range(0,5):
                    print('inserting data into unit_off_meassurements table....')
                    data_11 = (names[k],abbreviation[k])
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    unit_of_measurement_table_id +=1
            # offerings
            if(i == offerings_query):
                offerings_table_id = 1
                unit_of_measurement_id  = [1,1,2,5,4,5,4,2,3,1,5,4,3,2,1]
                offering_sub_category_id = [1,1,1,3,3,4,5,6,6,7,8,7,9,9,10]
                vendor_id = [1,1,2,5,1,5,5,4,2,3,1,5,4,3,2]
                offers_names = ["Professional DSLRs"," Mirror less cameras","Compact cameras",
                                "Speakers","Microphones","Live bands and musicians",
                                "Gourmet Delights Supply","Savory Bites Food Services","Gulaab Jam",
                                "LiquidLux Beverage Distributors","ThirstQuenchers Drink Supplies","Wine",
                                "Elegant Occasions Decor Supply","Aesthetic Ensembles Essentials","EventScapes Decoration Depot"
                                ]
                cgst_values = [11.05,12.387,13.179,14.587,15.104,12.0,33.0,15.0,66.0,11.05,12.387,13.179,14.587,15.104,12.0]
                sgst_values = [13,18,19,11,11,13,18,19,13,18,19,11,11,13,18]
                igst_values = [13,18,19,13,18,19,11,11,13,18,13,18,19,11,11]
                actual_price = [22.125,858.123,785.124,996.12,1425.22,858.123,785.124,996.12,1425.22,22.125,858.123,785.124,996.12,1425.22,858.123]
                discount_price = [10,12,14,33,10,12,14,33,10,12,14,33,10,12,14]
                quantity = [33,44,55,10,22,33,44,55,33,44,55,10,22,33,44]
                tags = ["Fast and Reliable","24/7 Customer Support","Secure and Private","Free Shipping","Expert Consultation","Fast and Reliable","24/7 Customer Support","Secure and Private","Free Shipping","Expert Consultation","Fast and Reliable","24/7 Customer Support","Secure and Private","Free Shipping","Expert Consultation"]
                sku = ["CAM001", "MUS002", "FOO003", "DEC004", "DRI005", "EVE006", "LIV007", "PHO008", "FLO009", "BAR010", "LIG011", "DEL012", "PAR013", "DJ014", "STF015"]
                hsn_codes = ["HSN Code: 8517","HSN Code: 6203","HSN Code: 3304","HSN Code: 3004","HSN Code: 8415","HSN Code: 8517","HSN Code: 6203","HSN Code: 3304","HSN Code: 3004","HSN Code: 8415","HSN Code: 8517","HSN Code: 6203","HSN Code: 3304","HSN Code: 3004","HSN Code: 8415"]
                sac_code = ["SAC Code: 85178","SAC Code: 8203","SAC Code: 4304","SAC Code: 7004","SAC Code: 5415","SAC Code: 8517","SAC Code: 6203","SAC Code: 3304","SAC Code: 3004","SAC Code: 8415","SAC Code: 8517","SAC Code: 6203","SAC Code: 3304","SAC Code: 3004","SAC Code: 8415"]
                
                offerings_description = ["Your go-to source for cutting-edge camera technology and equipment, offering a wide range of cameras and accessories to capture your moments with precision and clarity.",
                                        "Find professional-grade camera gear and equipment designed to meet the demands of photographers and videographers seeking exceptional performance and reliability.",
                                        "Discover a fusion of functionality and innovation with our camera equipment, meticulously crafted to help you achieve stunning results and focus on your creative vision.",
                                       
                                        "We provide top-notch music equipment and instruments to unleash the melodic magic, enabling musicians and performers to create unforgettable experiences.",
                                        "Find your rhythm with our premium music gear selection, catering to the needs of DJs, producers, and music enthusiasts who value precision and creativity.",
                                        "Enhance your events with our comprehensive entertainment supplies, including lighting, audio equipment, and special effects, ensuring every performance receives a standing ovation.",
                                    
                                        "Elevate your dining experience with our carefully selected food essentials, offering a range of savory delights to satisfy your taste buds.",
                                        "Discover a world of epicurean pleasures with our provisions, offering carefully curated ingredients and culinary delights for gastronomic adventures.",
                                        "We provide a fusion of flavors and culinary creativity, offering catering supplies that elevate every dish and make your events a flavorful success.",
                                        
                                        "Beat the heat and satisfy your thirst with our refreshing drink supplies, providing a variety of beverages to keep you hydrated and invigorated.",
                                        "Raise a toast to great taste with our curated beverage selection, ensuring that every sip is a celebration of flavors and enjoyment.",
                                        "Unleash your inner mixologist with our assortment of drink supplies and ingredients, empowering you to craft exquisite cocktails and mixology creations.",
                                        
                                        "Transform your events into visually stunning experiences with our essential decor elements, carefully curated to reflect your unique aesthetic vision.",
                                        "From backdrops to centerpieces, we provide a diverse range of decorations to turn any venue into a picturesque event scape that captivates your guests.",
                                        "Let us weave a touch of enchantment into your events with our enchanting decor options, leaving your guests spellbound and creating lasting memories."
                ]
                
                for k in range(0,15):
                    print('inserting data into offerings table....')
                    data_11 = (offers_names[k],offerings_description[k][:150],offerings_description[k],cgst_values[k],
                    sgst_values[k],igst_values[k],
                    actual_price[k],discount_price[k],random_boolean_for_offering[k],random_boolean_for_offering[k],unit_of_measurement_id[k],
                    quantity[k],offering_sub_category_id[k],vendor_id[k],sku[k],hsn_codes[k],sac_code[k],random_boolean_for_offering[k],tags[k]
                        )
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    offerings_table_id +=1
                    

                
            # add_ons_query table
            if(i == add_ons_query):
                offerings_id_list = [1,1,5,3,3]
                files_id_list = [1,4,2,4,5]
                add_ons_names = ["Wide-angle lens",
                "Guitar pedals and effects",
                    "Cutting board,Mixing bowls,Air fryer",
                    "Wine glasses,Bar spoon,Insulated travel mugs",
                    "String lights,Balloon arches,Letter banners"
                    ]
                add_ons_table_short_description = [
                    "Capture more of the world in a single frame with a wide-angle lens. Expand your perspective and embrace sweeping vistas, architectural marvels, and group shots with ease.",
                    "Achieve atmospheric textures with ambient reverbs and ethereal modulation",
                    "A cutting board for safe food prep, versatile mixing bowls for seamless ingredient prep, and an air fryer for healthier, crispy meals. Elevate your cooking experience today!",
                    "Enhance your drinking experience with elegant wine glasses, a versatile bar spoon for mixing cocktails, and insulated travel mugs to enjoy your beverages on the go",
                    "Create a captivating atmosphere with enchanting string lights, add a touch of whimsy with stunning balloon arches, and personalize your space with charming letter banners. "
                ]
                add_ons_table_long_description = [
                    "Capture more of the world in a single frame with a wide-angle lens. Expand your perspective and embrace sweeping vistas, architectural marvels, and group shots with ease.",
                    "Achieve atmospheric textures with ambient reverbs and ethereal modulation",
                    "A cutting board for safe food prep, versatile mixing bowls for seamless ingredient prep, and an air fryer for healthier, crispy meals. Elevate your cooking experience today!",
                    "Enhance your drinking experience with elegant wine glasses, a versatile bar spoon for mixing cocktails, and insulated travel mugs to enjoy your beverages on the go",
                    "Create a captivating atmosphere with enchanting string lights, add a touch of whimsy with stunning balloon arches, and personalize your space with charming letter banners. "
                ]
                price_in_add_ons = [12000.0,5561.11,225.0,6641.10,7787.0012]
                add_ons_table_id = 1
                for k in range(0,5):
                    print('inserting data into add_ons_query table....')
                    data_11 = (add_ons_names[k],add_ons_table_short_description[k][:150],add_ons_table_long_description[k],files_id_list[k],offerings_id_list[k],price_in_add_ons[k])
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    add_ons_table_id += 1

                # add_on_category_add_ons
            if(i == add_on_category_add_ons_query):
                # print(query_list[i])
                add_on_category_add_ons_table_id = 1
                add_ons_table_id_list = [1,1,2,3,5,4]
                for k in range(0,5):
                    print('inserting data into add_on_category_add_ons_query table....')
                    data_11 = (add_on_category_add_ons_table_id,add_ons_table_id_list[k])
                    cursor.execute(i,data_11)
                    connection_object.commit()
                    add_on_category_add_ons_table_id +=1
                    
            # coupons
            if(i == coupons_query):
                # print(query_list[i])
                coupon_names = ["SUMMER15","FREESHIP","SAVEMORE10","FLASHSALE20","FLASHSALE20"]
                coupon_codes = ["SF2023","FSHIP50","SAVE20NOW","FS25OFF","FIRST15NEW"]
                coupon_types = ["Discount Coupons","Fixed Amount Discount Coupons","Free Shipping Coupons","New Customer Coupons","Loyalty Reward Coupons"]
                coupon_description = [
                    "Enjoy exclusive savings with our discount coupons. Apply them at checkout to receive a percentage or specific amount off your purchase, making it more affordable and rewarding.",
                    "Get instant savings with our fixed amount discount coupons. Simply apply the coupon code at checkout to receive a specific monetary discount on your order, regardless of the total purchase amount.",
                    "Say goodbye to shipping fees with our free shipping coupons. Apply the coupon code during checkout to have your order delivered right to your doorstep at no additional cost.",
                    "Welcome to our community! As a new customer, enjoy special savings with our new customer coupons. Apply the code at checkout to receive a discount on your first purchase and start your shopping experience with great value.",
                    "We value your loyalty! Earn rewards with our loyalty program and receive loyalty reward coupons. Redeem these coupons for exclusive discounts or special perks as a token of our appreciation for your continued support."
                ]
                maximum_coupons = [1,2,5,7,1]
                coupons_table_id = 1
                for k in range(0,5):
                    print("data inserting into coupons")
                    coupons_table_data = (coupon_names[k],coupon_codes[k],faker.future_date(),coupon_types[k],1,maximum_coupons[k],coupon_description[k])
                    cursor.execute(i,coupons_table_data)
                    connection_object.commit()
                    coupons_table_id +=1


                # orders
            if(i == orders_query):
                total_cost = [212.012,556.21,785.00,1258.36,55.66]
                gst = [12.12,22.12,55.33,10.57,66.012]
                discount = [12.35,78.0,125.0,12.64,23.1]
                coupon_discount = discount
                coupon_discount.sort()
                delivery_charges  = total_cost
                delivery_charges.sort()
                event_manger_cost = [780.1144,789.54200,124.8723655,145.723,155.021]
                orders_table_id = 1
                order_address_list  = [1,1,2,2,4]
                coupon_id_list = [1,4,3,5,5]
                customer_id_list = [1,2,3,3,3]
                for k in range(0,5):
                    print("data inserting into orders")
                    orders_table_data = (
                            coupon_id_list[k],total_cost[k],
                            gst[k],discount[k],coupon_discount[k],
                            faker.future_datetime(),delivery_charges[k],order_address_list[k],
                            random_boolean[k],event_manger_cost[k],
                            customer_id_list[k])
                    cursor.execute(orders_query,orders_table_data)
                    connection_object.commit()
                    orders_table_id +=1 

                # statuses
            if(i == statuses_of_orders_query):
                # print(query_list[i])
                statuses_of_orders_table_id = 1
                statuses_id_list = [1,1,3,3,3]
                statuses_of_orders_table_description = [
                    "The order has been placed and is awaiting processing or confirmation.",
                    "The order is being prepared, verified, and fulfilled by the seller.",
                    "The order has been packed and handed over to the shipping carrier for delivery.",
                    "The order has been packed and handed over to the shipping carrier for delivery.",
                    "The order has been packed and handed over to the shipping carrier for delivery."
                ]
                order_id = 5            
                for k in range(0,5):
                    print("data inserting into statuses_of_orders")
                    statuses_of_orders_table_data = (order_id,statuses_id_list[k],statuses_of_orders_table_description[k][:150],statuses_of_orders_table_description[k])
                    cursor.execute(i,statuses_of_orders_table_data)
                    connection_object.commit()
                    statuses_of_orders_table_id += 1
                    order_id -= 1

            # orders_statusses Table
            if(i == order_status_query):
                # print(query_list[i])
                order_status_table_id = 1
                index_46 = 5
            
                status_codes = ["100","200","300","400","500"]
                order_status_names = ["Pending","Processing","Shipped","Delivered","Cancelled"]
                order_status_table_description = [
                    "The order has been placed and is awaiting processing or confirmation.",
                    "The order is being prepared, verified, and fulfilled by the seller.",
                    "The order has been packed and handed over to the shipping carrier for delivery.",
                    "The order has been successfully delivered to the customer's specified address.",
                    "The order has been cancelled either by the customer or the seller."
                ]
                customer_status_names = ["Active","Inactive","Prospective","Suspended","Churned"]
                remarks = ["Delayed due to inventory shortage","Address verification required","Customer requested change in delivery date","Item out of stock - awaiting restock","Refund processed, awaiting confirmation"]
                
                for k in range(0,5):
                    print("Data inserting into orders_statuses")
                    order_status_table_data = (status_codes[k],order_status_names[k],order_status_table_description[k],remarks[k][:45],random_boolean[k],customer_status_names[k])
                    cursor.execute(i,order_status_table_data)
                    connection_object.commit()
                    order_status_table_id += 1
                    index_46 -=1

            # invoices
            if(i == invoice_query):
                invoice_table_id = 1
                order_id = 5
                invoice_number = ["INV-2023-001","23567","INV210625"," 1002/2023","INV-4589-AC"]
                payments_status = ["Pending","Authorized","Captured","Declined","Refunded"]
                invoices_description = [
                    "This invoice number follows a structured format, starting with INV to denote an invoice, followed by the year 2023 and a unique three-digit number 001. It helps identify and track the specific invoice associated with a transaction or purchase.",
                    "This invoice number is a numerical identifier assigned to an invoice. It serves as a unique reference for tracking and managing transactions, providing a straightforward and simple identification system.",
                    "This invoice number combines the letters INV to represent an invoice, followed by the date 210625 which represents June 25, 2021, in YYMMDD format. It offers a clear indication of the invoice's issuance date and aids in organizing and retrieving invoices efficiently.",
                    "This invoice number follows a date-based format, with 1002 representing the sequential number of the invoice and 2023 indicating the year of issuance. It offers a straightforward system for identifying and organizing invoices based on the date.",
                    "This invoice number includes the letters INV to designate an invoice, followed by the unique numbers 4589 and the letters AC. It provides a distinct identifier for the invoice, aiding in record-keeping and tracking transactions associated with it."
                ]
                for k in range(0,5):
                    print("Data inserting into invoices table ..")
                    invoice_table_data = (invoice_number[k],
                            invoices_description[k][:150],invoices_description[k],
                            order_id,payments_status[k])
                    cursor.execute(invoice_query,invoice_table_data)
                    connection_object.commit()       
                    invoice_table_id += 1
                    order_id -= 1

            # biddings
            if (i == biddings_query):
                # print(query_list[i])
                index_49 = 1
                index_50 = 5
                bidding_remarks = ["Bid Accepted","Outbid","Winning Bid","Reserve Not Met","Bid Rejected"]
                bidding_remarks = ["Vendor Bid","Customer Bid","Vendor Accepted","Vendor Bid","Customer Bid"]
                # print(query_list[i])
                for k in range(0,5):
                    print("Data inserting into biddings")
                    data = (random_boolean[k],faker.future_datetime(),index_50,random_boolean[k],random_boolean[k],bidding_remarks[k])
                    cursor.execute(i,data)
                    connection_object.commit()
                    index_49 += 1
                    index_50 -= 1

                # event_categories
            if(i == event_categories_query):
                event_categories_table_id = 1
                files_id = 5
                event_categories_names = ["Wedding","Birthday","DJ Party","Music Concert","Festival"]
                event_categories_table_description = ["Create your perfect wedding day with our personalized planning services. From venue to decor, we handle every detail for a stress-free experience.",
                                                     "Celebrate your special day in style with our exceptional birthday event planning services. From themed decorations to customized cakes and entertainment, we'll ensure every detail is taken care of. Let us make your birthday unforgettable and create memories that will last a lifetime.",
                                                     "Get ready to dance the night away with our electrifying DJ party experience. Our talented DJs will spin the hottest tracks, creating a high-energy atmosphere that will keep you on the dance floor",
                                                     "Unleash your passion for music at our electrifying music concerts. Experience unforgettable performances by top artists, surrounded by an energetic crowd. Get ready for an incredible night of live music that will leave you craving for more.",
                                                     "Immerse yourself in a world of music, art, and culture at our vibrant festival. Join us for a celebration of creativity, featuring live performances, interactive installations, and a diverse range of experiences"
                                                    ]
                for k in range(0,5):
                    print("data inserting into event_categories")
                    event_categories_table_data = (event_categories_names[k],event_categories_table_description[k][:150],event_categories_table_description[k],files_id)
                    cursor.execute(i,event_categories_table_data)
                    connection_object.commit()
                    event_categories_table_id += 1
                    files_id -= 1
                
            # event_categories_offerings
            if(i == event_category_offerings):
                # print(query_list[i])
                
                index_53 = 1
                offering_id_list = [2,2,3,3,4]
                bidding_remarks = ["Bid Accepted","Outbid","Winning Bid","Reserve Not Met","Bid Rejected"]
                # event_categories_offerings = ["Music Events","Sports Events","Business Conferences","Arts and Culture Events","Charity and Fundraising Events"]
                # print(query_list[i])
                for k in range(0,5):
                    print("data inserting into event_categories_offerings")
                    data = (index_53,offering_id_list[k])
                    cursor.execute(i,data)
                    connection_object.commit()
                    index_53 += 1
                    
                    
            # wishlists
            if(i == wish_list):
                # print(query_list[i])
                index_55= 1
                for k in range(0,5):
                    print("data inserting into wish_list")
                    data = (index_55,index_55)
                    cursor.execute(i,data)
                    connection_object.commit()
                    index_55 += 1
                
                # offering_files
            if(i == offering_files):
                # print(query_list[i])

                index_56= 1
                for k in range(0,5):
                    print("data inserting into offering_files...")
                    data = (index_56,index_56)
                    cursor.execute(i,data)
                    connection_object.commit()
                    index_56 += 1
            
            # order_add_ons
            if(i == order_add_ons):
                # print(query_list[i])
                order_add_ons_table_id = 1
                add_ons_id_list = [1,1,1,4,4]
                quantity = [5,8,6,10,22,33]
                for k in range(0,5):
                    print("data inserting into order_add_ons table.....")
                    data = (order_add_ons_table_id,add_ons_id_list[k],quantity[k])
                    cursor.execute(i,data)
                    connection_object.commit()
                    order_add_ons_table_id += 1
            
            # orders_offerings
            if(i == orders_items_query):
                # print(query_list[i])
                order_items_quantity = [1,2,5,4,9]
                orders_items_table_id= 1
                offering_id_list = [1,1,1,2,4]
                for k in range(0,5):
                    print("data inserting into order_items table.....")
                    data = (orders_items_table_id,offering_id_list[k],order_items_quantity[k])
                    cursor.execute(i,data)
                    connection_object.commit()
                    orders_items_table_id += 1
            
            # cart_items
            if(i == cart_items_query):
                # print(query_list[i])
                cart_items_table_id = 1
                cart_id_list = [1,3,1,1,4]
                offering_id_list = [1,2,3,3,5]
                quantity = [5,8,6,10,22,33]
                for k in range(0,5):
                    print("data inserting into cart_items table ....")
                    data = (cart_id_list[k],offering_id_list[k],quantity[k])
                    cursor.execute(i,data)
                    connection_object.commit()
                    cart_items_table_id += 1
                    
            
            # vendors_files
            if(i == vendors_files):
                index_62 = 1
                quantity = [5,8,6,10,22,33]
                for k in range(0,5):
                    print("data inserting into vendors_files table ....")
                    data = (index_62,index_62)
                    cursor.execute(i,data)
                    connection_object.commit()
                    index_62 += 1
                    
        # no_of_query_counter += 1

            if (i == confirmed_orders_query):
                confirmed_orders_table_id = 1
                active_status_list = [1,1,1,1,2]
                orders_id = 1
                for k in range(0,5):
                    print("data inserting into confirmed orders table ....")
                    confirmed_orders_table_data = (active_status_list[k],orders_id)
                    cursor.execute(i,confirmed_orders_table_data)
                    connection_object.commit()
                    confirmed_orders_table_id +=1
                    orders_id +=1
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
    # except Exception as Err:
    #     print(Err)

inserting_data_into_tables()
connection_object.close()