from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine("sqlite:///C:\Users\Alex\Documents\GitHub\Microblog_Flask/app.db")

m = MetaData()
m.reflect(engine)
for table in m.tables.values():
    print(table.name)
    for column in table.c:
        print(column.name)
