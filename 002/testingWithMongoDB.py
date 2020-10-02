import pymongo


# client = pymongo.MongoClient("mongodb+srv://<dev>:<YEvHB5lRfrbhvm26>@cluster0.dw0dx.mongodb.net/<daysofcode>?retryWrites=true&w=majority")
# db = client.test


client = pymongo.MongoClient("mongodb://dev:<YEvHB5lRfrbhvm26>@100daysofcode-shard-00-00.dw0dx.mongodb.net:27017,100daysofcode-shard-00-01.dw0dx.mongodb.net:27017,100daysofcode-shard-00-02.dw0dx.mongodb.net:27017/<daysofcode>?ssl=true&replicaSet=atlas-13tzby-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

dblist = client.list_database_names()
if "daysofcode" in dblist:
  print("The database exists.")


# print(db.list_database_names())

