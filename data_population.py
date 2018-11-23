from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

MyFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(MyFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepizza = MenuItem(name = "Cheese Pizza",
                description = "Made with all natural + \
                ingredients and fresh mozzarella",
	            course = "entree",
	            price = "$8.99", 
	            restaurant = MyFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()