import sys
class ToDo():
    def __init__(self):
        self.todo_list = []
        self.done_list = []
        self.control = 0
        self.new_todo = 0
        self.data = 0
        self.data2 = 0
        self.predone_list = []
        self.data_append = 0
        self.line_to_delete = 0
        self.data_write = 0
        self.line_to_check = 0
        self.todo_checking_before = 0
        self.todo_checking_after = 0
    def controller(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "-l":
                self.control = 1
                self.database_reader()
            elif sys.argv[1] == "-a":
                if len(sys.argv) > 2:
                    self.new_todo = sys.argv[2]
                self.control = 2
                self.database_reader()
            elif sys.argv[1] == "-r":
                if len(sys.argv) > 2:
                    self.line_to_delete = sys.argv[2]
                elif len(sys.argv) == 2:
                    self.no_remove_printer()
                self.control = 3
                self.database_reader()
            elif sys.argv[1] == "-c":
                if len(sys.argv) > 2:
                    self.line_to_check = sys.argv[2]
#                elif len(sys.argv) == 2:
#                    self.no_remove_printer()
                self.control = 4
                self.database_reader()
            else:
                if len(sys.argv) == 2:
                    self.argument_printer()
                self.help_printer()
        else:
            self.help_printer()

    def help_printer(self):
        print("Python Todo application")
        print("=======================")
        print("")
        print("Command line arguments:")
        print("  -l   Lists all the tasks")
        print("  -a   Adds a new task")
        print("  -r   Removes an task")
        print("  -c   Completes an task")

    def normal_printer(self):
        a = 1
        if self.todo_list == []:
            print("No todos for today! :)")
        else:
            for todo in self.todo_list:
                if todo == "":
                    pass
                else:
                    print(str(a) + " - " + str(todo))
                    a +=1

    def no_add_printer(self):
        print("Unable to add: no task provided")

    def no_remove_printer(self):
        print("Unable to remove: no index provided")

    def no_remove_no_integer(self):
        print("Unable to remove: index is not a number")

    def argument_printer(self):
        print("\nUnsupported argument \n")

    def database_reader(self):
        self.data = open("todo_db.txt", "r")
        self.data2 = self.data.readlines()
        self.todo_list = [i.split("Đ")[0] for i in self.data2]
        while True:
            try:
                self.predone_list = [i.split("Đ")[1] for i in self.data2]
                break
            except:
                break
        while True:
            try:
                self.done_list = [i.split("\n")[0] for i in self.predone_list]
                break
            except:
                break
        if self.control == 1:
            self.normal_printer()
        if self.control == 2:
            self.add_todo_list()
        if self.control == 3:
            self.line_deleter()
        if self.control == 4:
            self.checker()

    def add_todo_list(self):
        if self.new_todo == 0:
            self.no_add_printer()
        else:
            self.data_append = open("todo_db.txt", "a")
            self.data_append.write(str(self.new_todo) + "Đ" + "\n")

    def line_deleter(self):
        while True:
            try:
                if int(self.line_to_delete) >= 1 and int(self.line_to_delete) < len(self.data2):
                    del self.data2[int(self.line_to_delete)-1]
                    self.data_write = open("todo_db.txt", "w")
                    for lines in self.data2:
                        self.data_write.write(lines)
                if int(self.line_to_delete) > len(self.data2):
                    print("Unable to remove: index is out of bound")
                break
            except:
                break
        if isinstance(self.line_to_delete, str) == True:
            self.no_remove_no_integer()

    def checker(self):
        while True:
            try:
                if int(self.line_to_check) >= 1 and int(self.line_to_check) < len(self.data2):
                    self.todo_checking_before = self.data2[(int(self.line_to_check)-1)].split("Đ")[0]
                    self.todo_checking_after =  ("Đ" + str(self.todo_checking_before))
                break
            except:
                break


        print(self.todo_checking_after)
teve = ToDo()
teve.controller()
