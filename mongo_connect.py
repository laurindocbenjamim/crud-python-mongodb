from pymongo import MongoClient

user='root'
password=''
host='localhost'
#connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)
connecturl = "mongodb://{}:27017/?authSource=admin".format(host)

# Connect ro mongo DB
print("Connection to mongo server")
connection = MongoClient(connecturl)

#print(connection)

# Get database list 
print("Getting list of databases")
dbs = connection.list_database_names()

# Print the database list
for db in dbs:
    print(db)


# Selection the training database

db = connection.training

#print(db)

# Select the 'python' collection

collection = db.python




print("Closing the connection to the mongo db")

#Close the server connection
connection.close()