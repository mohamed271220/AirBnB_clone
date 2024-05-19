import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all method
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        new method
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        save method
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding = "utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        reload method
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding = "utf-8") as f:
                try:
                    new_dict = json.load(f)
                    for key, value in new_dict.items():
                        obj = eval(value["__class__"])(**value)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
