import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "52.63.112.33"
name = "sa"
password = "TChangeh&33plz7@L"
db_name = "SSIS"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def handler(event, context):
    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table [dbo].[Employee] ( EmpID  int, Name varchar(255))")
        cur.execute('insert into [dbo].[Employee] (EmpID, Name) values(1, "Joe")')
        cur.execute('insert into [dbo].[Employee] (EmpID, Name) values(2, "Bob")')
        cur.execute('insert into [dbo].[Employee] (EmpID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from [dbo].[Employee]")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)
