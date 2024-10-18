import json
import sys

task_id = 0

class Task_Tracker:
    def __init__(self, id , description, status, createdAt, updatedAt):
        global task_id
        task_id += 1
        self.id = task_id
        self.description = description 
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def add(self):
        task_data = {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updatedAt" : self.updatedAt
        }
        # print(task_data)

        # print (f" data ---> {task_data}")
        with open("Task_Tracker.json", "r") as f:
            # lines = [line for line in f.readlines() if line.strip('\n')]
            # print(lines)
            # if lines:
            #     print("ok")
            # else:
            #     print("not ok")
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                print("not ok")

            # print(len(data))
            # if len(data):
            #     print("there 's no data")
            # else :
            #     print(data)
            # print(data)
            # json.dump(task_data, f, indent=4)
            # f.write("\n")
            

    # def update():
    #     pass
    # def delete():
    #     pass
    # def mark_in_progress():
    #     pass
    # def mark_done():
    #     pass
    # def list_():
    #     pass
    # def list_done():
    #     pass
    # def list_todo():
    #     pass
    # def list_in_progress():
    #     pass
    

# def Task_Cmds():

#     global C1
    
#     if args[0] == "add":
#         C1.add()
#     elif args[0] == "update":
#         C1.update()
#     elif args[0] == "delete":
#         C1.delete()
#     elif args[0] == "mark-in-progress":
#         C1.mark_in_progress()
#     elif args[0] == "mark-done":
#         C1.mark_done()
#     elif args[0] == "list":
#         C1.list_()
#     elif args[0] == "list done":
#         C1.list_done()
#     elif args[0] == "list todo":
#         C1.list_todo()
#     elif args[0] == "list in-progress":
#         C1.list_in_progress()
#     else:
#         print(" the cmd that u enter is not available in th ecmds list , please try again")


def join_args(args):
    result = " ".join(args)
    return result




args = sys.argv[1:]
C1 = Task_Tracker(id , join_args(args[1:]), "present", "1", "3")
# Task_Cmds()
print (f"u entered -->  {args}")

C1.add()
