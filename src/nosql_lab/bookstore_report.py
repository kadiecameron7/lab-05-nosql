#!/usr/bin/env python3

import os
import logging
import pymongo

MONGODB_ATLAS_URL = os.environ.get("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.environ.get("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.environ.get("MONGODB_ATLAS_PWD")


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    """Create a report of authors and their books."""
    client = None
    try: # Connect to MongoDB Atlas
        client = pymongo.MongoClient(
            MONGODB_ATLAS_URL, 
            username=MONGODB_ATLAS_USER, 
            password=MONGODB_ATLAS_PWD)
        logging.info("Connected to MongoDB Atlas.")
        db = client["bookstore"] # Access the bookstore database
        authors = db["authors"] # Access the authors collection
        books = db["books"] # Access the books collection   
        author_ids = ["author_002", "author_003", "author_005"]

        n = authors.count_documents({"_id": {"$in": author_ids}}) #Count the number of authors with the given IDs
        print(f"Authors: {n}") # Print the number of authors found

        for author in authors.find({"_id": {"$in": author_ids}}):
            print(author["name"]) # Print author name
            for book in books.find({"author_ids": author["_id"]}):
                print(f"   Book: {book['title']} ({book['published_year']})") # Print each book title and published year

    except Exception as e: # Handle exceptions and log errors
        logging.error(f"An error occurred: {e}")
    finally:
        if client is not None:
            client.close()
            logging.info("MongoDB connection closed.") # Log that connection has been closed

if __name__ == "__main__": # Run the main function if this script is executed directly
    main()