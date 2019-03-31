# Log Analysis

This project is to build a python and SQL reporting tool that summarizes
data from a large postgres database.

## Prerequisite

This project makes use of  Linux-based virtual machine (VM) as the preceding lessons.

### Vagrant
Vagrant is the software that configures the VM and lets you share files
between your host computer and the VM's filesystem.

### VirtualBox
VirtualBox is the software that actually runs the virtual machine.The supported version
of VirtualBox to install is version 5.1. Newer versions do not work with
the current release of Vagrant.

### VM Configuration
Download this repo: https://github.com/udacity/fullstack-nanodegree-vm
and from your terminal `cd` to the vagrant folder

## Start the Virtual Machine
From the vagrant subdirectory run the command:
```sh
vagrant up
```
When `vagrant up` is finished running run the command below to log int to
the installed Linux VM:
```sh
vagrant ssh
```

## Download the data and Clone this Repo

Download the data here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Unzip it and  put the `newsdata.sql` into the vagrant folder and clone
this project inside the vagrant folder

## Load the data
To load the data, `cd` into the `vagrant` directory and use the command:
```sh
psql -d news -f newsdata.sql
```
More information about the command:
* `psql` - the PostgresSQL command line program
* `-d news` - connect to the database news
* `-f newsdata.sql` - run the SQl statements in the file newsdata.sql

Running the above command will connect to the installed database server
and execute the SQl commands in the downloaded file, creating tables and
populating them with data.

## Explore The data
Once the data load into the database, connect to the database with this
command `psql -d news` and explore the tables using the `\dt` and
`\d table_name` commands and `select` statements

The database includes 3 tables:
* Authors
* Articles
* Log

## Run

To run the program from vagrant run `python3 report.py` from the command
 line

## Report Information
The objective of this project is  to create a reporting tool that prints
out reports based on the data in the database. This reporting tools is just
a simple Python program using the `psycopg2` module to connect to the database.

### What are we reporting
Here are the questions the reporting tool answer:

1. **What are the most popular tree articles of all time?**
Which articles have been accessed the most?  The program present this information as a sorted
list with the most popular article at the top.

2. **Who are the most popular article authors of all time?**
When summing up all of the articles each author has written, which authors
get the most page views? The program present this as a sorted list with
 the most popular author at the top.

3. **On which days did more than 1% of requests lead to errors?** The log
table include a column status that indicates the HTTP status code that
the news site sent to the user's browser.
