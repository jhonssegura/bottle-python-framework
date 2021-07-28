import sqlite3
conn = sqlite3.connect('animals.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE animals (id INTEGER PRIMARY KEY, name char(20) NOT NULL, type char(20) NOT NULL)")
conn.execute("INSERT INTO animals (name,type) VALUES ('Ellie','Elephant')")
conn.execute("INSERT INTO animals (name,type) VALUES ('Python','Snake')")
conn.execute("INSERT INTO animals (name,type) VALUES ('Zed','Zebra')")
conn.execute("INSERT INTO animals (name,type) VALUES ('Richard','Lion')")
conn.commit()