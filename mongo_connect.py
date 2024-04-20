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


#Create a sample document
doc = {
    "lab": "Accessing mongo using Python",
    "subject": "No SQL Databases"
}
doc2 = [
    {"database":"a database contains collections"},
    {"collection":"a collection stores the documents"},
    {"document":"a document contains the data in the form or key value pairs."},

]

print("Inserting data into collection")
db.collection.insert_one(doc)



print("Closing the connection to the mongo db")

#Close the server connection
connection.close()