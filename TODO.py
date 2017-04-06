import sys
def controller():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-l":
            return 1
        elif sys.argv[1] == "-a":
            return 2
        elif sys.argv[1] == "-r":
            return 3
        elif sys.argv[1] == "-c":
            return 4
        else:
            help_printer()
    else:
        help_printer()

def help_printer():
    print("Python Todo application")
    print("=======================")
    print("")
    print("Command line arguments:")
    print("  -l   Lists all the tasks")
    print("  -a   Adds a new task")
    print("  -r   Removes an task")
    print("  -c   Completes an task")


controller()
print(controller())
