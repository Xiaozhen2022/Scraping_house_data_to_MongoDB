setup MongoDB: 
download: https://www.mongodb.com/try/download/community-kubernetes-operator 
issues:
How to cover the data in MongoDB when inserting?

How to implement fuzzy query?
db.users.find({ name: { $regex: /John/ } })
<!-- Fuzzy queries that ignore capital and lower case -->
db.users.find({ name: { $regex: /searchString/, $options: 'i' } }) 

How to delete data met condition in collection?
db.users.deleteOne({ name: "John" })

How to delete all data in collection？
db.collectionName.delete_many({})

