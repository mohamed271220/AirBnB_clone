#!/usr/bin/python3
"""
base model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self):
        """
        __init__ method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """
        save method
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        to_dict method
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict

    def __str__(self):
        """
        __str__ method
        """
        cn = self.__class__.__name__
        return "[{}] ({}) {}".format(cn, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "1st"
    my_model.my_number = 555
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
