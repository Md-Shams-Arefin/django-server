# import pymongo

# url = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(url)

# db = client['test_mongo']

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# # Replace the placeholder with your Atlas connection string
# uri = "mongodb://localhost:27017"

# # Set the Stable API version when creating a new client
# client = MongoClient(uri, server_api=ServerApi('1'))
                          
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     db = client['test_mongo']
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)