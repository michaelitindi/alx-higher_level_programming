-- creates database hbtn_0d_usa
-- creates table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256));