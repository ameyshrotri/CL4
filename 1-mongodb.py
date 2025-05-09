
#this code should be executed in  terminal

# 8. Open MongoDB shell
mongosh

# ----------------------------------------------------
# 📦 MongoDB Shell: Create DB, Insert, Query, Delete
# ----------------------------------------------------

# Use or create a new database
use studentDB

# Insert one document
db.students.insertOne({
  name: "Amey",
  age: 22,
  course: "Computer Engineering"
})

# Insert multiple documents
db.students.insertMany([
  { name: "Ravi", age: 23, course: "IT" },
  { name: "Sneha", age: 21, course: "AI/ML" }
])

# Show collections
show collections

# Show all documents
db.students.find()

# ----------------------------------------------------
# 🗑️ Delete Commands
# ----------------------------------------------------

# Delete students younger than 22
db.students.deleteMany({ age: { $lt: 22 } })

# Delete students aged 22 or younger
db.students.deleteMany({ age: { $lte: 22 } })

# Delete all students named 'Ravi'
db.students.deleteMany({ name: "Ravi" })

# ----------------------------------------------------
# ✅ Helpful Extras
# ----------------------------------------------------

# Pretty print results
db.students.find().pretty()

# Count documents
db.students.countDocuments()

# Update document
db.students.updateOne(
  { name: "Amey" },
  { $set: { status: "active" } }
)

# Drop collection
db.students.drop()
