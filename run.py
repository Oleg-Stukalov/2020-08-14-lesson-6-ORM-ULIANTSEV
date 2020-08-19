import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import Shop

DB_PATH = 'postgresql+psycopg2://netology:netology@localhost/books_shop2'
engine = sq.create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

if __name__ == '__main__':
    session = Session()
    all_shops = session.query(Shop).all()
    print(all_shops)
    print(all_shops[0].name)

