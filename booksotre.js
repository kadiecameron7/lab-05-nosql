// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
// paste your drop and insertMany commands here
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
// paste your drop and insertMany commands here
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
// paste your find commands here
db.authors.find()
db.books.find()

// Step 6: insert two new books
// paste your insert commands here
db.books.insertMany([
    {title: "The Outsiders", 
        published_year: 1967, 
        author_ids: ["author_004"]}, 
    {title: "The Perks of Being a Wallflower", 
        published_year: 1999, 
        author_ids: ["author_005"]
    }])

// Step 7: add missing authors
// paste your insert commands here
db.authors.insertMany([
    {_id: "author_004",
        name: "S. E. Hintin", 
        nationality: "United States", 
        bio: { short: "She wrote a book", 
            long: "She wrote the book the Outsiders."}
        }, 
    {_id: "author_005", 
        name: "Stephen Chbosky", 
        nationality: "United States", 
        bio: {short: "He wrote a book.", 
            long: "He wrote the book the Perks of Being a Wallflower"}
        }])

// Step 8: filter books by a list of authors
// paste your find command here
db.books.find({authors_ids: {$in: ["author_001", "author_005"]}})
