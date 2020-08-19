import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    network = relationship('Network', backref='shop', cascade='all, delete-orphan')
    shop_id = sq.Column(sq.ForeignKey('shop.id', ondelete='CASCADE'))


class Network(Base):
    __tablename__ = 'network'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)


class Storage(Base):
    __tablename__ = 'storage'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    shop_id = sq.Column(sq.ForeignKey('shop.id', ondelete='CASCADE'))
