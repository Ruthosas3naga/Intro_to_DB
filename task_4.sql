-- File name: task_4.sql

-- Use the specified database
USE alx_book_store;

-- Query to get the full description of the table 'books'
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';


