from sqlalchemy import Column, Integer, String, Boolean, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from eapp import db, app

class BaseModel(db.Model):
    __abstract__ = True

    id= Column(Integer, primary_key= True, autoincrement=True)
    active = Column(Boolean, default=True)
class Category(BaseModel):
    name = Column(String(50), unique= True)
    products = relationship('Product', backref= 'category', lazy= True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = Column(String(255), nullable= False)
    description = Column(Text, nullable= True)
    price = Column(Float, default=0)
    image = Column(String(100), default= 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg')
    category_id = Column(Integer, ForeignKey(Category.id), nullable= False)

    def __str__(self):
        return self.name

if __name__ =='__main__':
    with app.app_context():
         db.create_all()
         #
         # c1 = Category(name = 'Mobile')
         # c2 = Category(name='Tablet')
         # c3 = Category(name='Laptop')
         # c4 = Category(name = 'Desktop')
         # db.session.add_all((c1, c2, c3))
         # db.session.commit()
