import sys
class ToDo():
    def __init__(self):
        self.todo_list = []
        self.done_list = []
        self.control = 0
    def controller(self):
        if len(sys.argv) == 2:
            if sys.argv[1] == "-l":
                self.control = 1
                self.database_reader()
            elif sys.argv[1] == "-a":
                self.control = 2
                self.database_reader()
            elif sys.argv[1] == "-r":
                self.control = 3
                self.database_reader()
            elif sys.argv[1] == "-c":
                self.control = 4
                self.database_reader()
            else:
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
                print(str(a) + " - " + str(todo))
                a +=1

    def database_reader(self):
        data = open("todo_db.txt", "r")
        data2 = data.readlines()
        self.todo_list = [i.split('Đ')[0] for i in data2]
        predone_list = [i.split('Đ')[1] for i in data2]
        self.done_list = [i.split('\n')[0] for i in predone_list]

        if self.control == 1:
            self.normal_printer()


teve = ToDo()
teve.controller()
