import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# create sql query and run right away with .exec()
# create_table_sql = QSqlQuery()
#
# create_table_sql.exec_(
#     """
#       CREATE TABLE ehsancontacts (
#           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
#           name VARCHAR(40) NOT NULL,
#           job VARCHAR(50),
#           email VARCHAR(40) NOT NULL
#       )
#       """
# )
# print(con.tables())
# after creation table, insert to it
# using static query execution
# name = "mohammad1"
# job = "Technical Lead"
# email = "mohammad12134@gmail.com"
#
# insert_query = QSqlQuery()
# isOk = insert_query.exec_(
#     f"""INSERT INTO ehsancontacts (name, job, email) VALUES ('{name}', '{job}', '{email}')"""
# )
#
# print(isOk)


# insert to table using dynamic query
# and prepare statement
# Creation a query for later execution using .prepare()
# insert_query_using_prepare_statement = QSqlQuery()
# insert_query_using_prepare_statement.prepare(
#     """
#     INSERT INTO ehsancontacts (
#     name,
#     job,
#     email
#     )
#     VALUES (?, ?, ?)
#     """
# )
#
# # sample data
# data = [
#     ("Ehsan", "Senior Web Developer", "ehsanmnz@gmail.com"),
#     ("Ali", "Project Manager", "ali@gmail.com"),
#     ("Majid", "Data Analyst", "majid@gmail.com"),
#     ("Reza", "Senior Python Developer", "Reza@gmail.com"),
# ]
#
# areOk = []
# for name, job, email in data:
#     insert_query_using_prepare_statement.addBindValue(name)
#     insert_query_using_prepare_statement.addBindValue(job)
#     insert_query_using_prepare_statement.addBindValue(email)
#     areOk.append(insert_query_using_prepare_statement.exec())

# print(areOk)

# retrieve data

select_query = QSqlQuery()
isOk = select_query.exec("SELECT * FROM ehsancontacts")
if isOk:
    while select_query.next():
        print(select_query.value(0), select_query.value(1), select_query.value(2), select_query.value(3))

if select_query.isActive():
    select_query.finish()
