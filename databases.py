from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, in_stock, product_type):
	product_object = Product(
        name=name,
        price=price,
        in_stock=in_stock,
        product_type=product_type )
	session.add(product_object)
 	session.commit()

#create_product("Black shirt", 15, True, "shirt")

def update_product(name, price, in_stock):
 	product_object=session.query(Product).filter_by(name=name).first()
 	product_object.price=price
 	product_object.in_stock=in_stock
 	session.commit()

#update_product_price("Black shirt", 10, False)

def delete_product(name):
	product_object=session.query(Product).filter_by(name=name).delete()
	session.commit()

def first_product():
	product_object=session.query(Product).first()
	return product_object

#delete_product("Black shirt")

def get_product(id):
  pass
