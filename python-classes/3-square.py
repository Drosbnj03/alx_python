"""This module houses a class that represents a square """
class Square:
    """Represents a Square with Size 
    size should be an integer and greater than zero"""
    def __init__(self,size=0):
        if not isinstance(size,int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            
    @property
    def size(self):
        '''public method: Returns the size of the square'''
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value,int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Public instance method: Returns the area of the square"""
        return (self.__size**2)
        