#!/usr/bin/python3
"""
console module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = '(hbnb) '
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        help_quit method
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """
        emptyline method
        """
        pass

    def do_create(self, line):
        """
        Create command to create a new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show command to print the string representation of an instance
        """
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Destroy command to delete an instance
        """
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()