#!/usr/bin/python3
""" class rectangle that inherfits from base """


from models.base import Base


class Rectangle(Base):
    """ class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x coordinate of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x coordinate of rectangle """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y coordinate of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y coordinate of rectangle """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """ prints rectangle with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ overriding the __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """  assigns a key/value argument to attributes:"""
        if args:
            att = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args[:len(att)]):
                setattr(self, att[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dict representation"""
        return{
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
