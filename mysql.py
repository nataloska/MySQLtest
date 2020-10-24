import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        # rows = [("John", 20, "2000-01-02 09:00:00"), 
        #         ("Sjoerd", 27, "1993-08-23 09:00:00"),
        #         ("Natalia", 35, "1985-02-07 09:00:00")]
        listofnames = ["John", "Sjoerd", "Natalia"]
        format_strings = ",".join(['%s']*len(listofnames))
        cursor.execute("delete from Friends where name in ({});".format(format_strings), listofnames)
        print(cursor.execute("select * from Friends;"))
        connection.commit()
        # cursor.execute(sql)
        # for row in cursor:
        #     print(row)

finally:
    connection.close()