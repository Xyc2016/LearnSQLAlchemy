from sqlalchemy import select, create_engine, MetaData, union

engine = create_engine(
    'mysql+mysqldb://xyc:xyc782826@localhost/classicmodels',echo=True
)
meta = MetaData(bind=engine)
meta.reflect()

