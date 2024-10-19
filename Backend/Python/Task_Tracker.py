import json
import sys
import datetime

class Task_Tracker:
    def __init__(self, id , description, status, createdAt, updatedAt):
        self.id = self.get_next_id()
        self.description = description 
        self.status = "todo"
        self.createdAt = str(datetime.datetime.now())
        self.updatedAt = updatedAt

    def getId(self):
        return self.id

    def get_next_id(self):
        
        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
            if data:
                return len(data) + 1
            else :
                return 1
        except (FileExistsError , json.decoder.JSONDecodeError):
            return 1

    def add(self):
        
        task_data = {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updatedAt" : self.updatedAt
            }
        try:
            with open("Task_Tracker.json", "r") as f:
                try:
                    data = json.load(f)
                    data.append(task_data)
                    print(data)
                    # json.dump(task_data, data, indent=4)
                    # print(data)
                    # data
                    # json.dump()
                    # json.dump(task_data, f, indent=4)

                except json.decoder.JSONDecodeError:
                    # print("Shite error or empty file")
                    data = [
                        {
                            "id" : self.id,
                            "description" : self.description,
                            "status" : self.status,
                            "createdAt" : self.createdAt,
                            "updatedAt" : self.updatedAt
                        }
                    ]
        except FileNotFoundError:
            data = []
        
        # data.append(task_data)

        with open("Task_Tracker.json", "w") as f:
            json.dump(data, f, indent=4)

    def update(self, id ,newdescription):

        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return 
        
        # if int(id) < 1 or int(id) > len(data):
        #     print("u enter a non valid id try again", file=sys.stderr)

        i = 0
        while i < len(data):
            if data[i]["id"] == int(id):
                data[i]["description"] =  join_args(newdescription)
                data[i]["updatedAt"] =  str(datetime.datetime.now())
            i+=1
        # if newdescription:
        #     data[int(id) - 1]["description"] =  join_args(newdescription)
        #     data[int(id) - 1]["updatedAt"]  = str(datetime.datetime.now())
        # else:
        #     print("u enter an update cmd zithout specifying new description .", file=sys.stderr)
                

        with open("Task_Tracker.json", "w") as f:
            json.dump(data, f, indent=4)

    def delete(self , id):

        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("the Task file not found")
            return
        
        new_data = []

        i = 0
        while i < len(data):
            if data[i]["id"] != int(id):
                new_data.append(data[i])
            i+=1

        
        with open("Task_Tracker.json", "w") as f:
            json.dump(new_data, f, indent=4)
            
    def mark_in_progress(self, id):

        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return 
        

        # data[int(id) - 1]["status"] = "in-progress"

        i = 0
        while i < len(data):
            if data[i]["id"] == int(id):
                data[i]["status"] =  "in-progress"
                data[i]["updatedAt"] =  str(datetime.datetime.now())
            i+=1

        with open("Task_Tracker.json", "w") as f:
            json.dump(data, f, indent=4)

    def mark_done(self, id):

        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return 
        
        i = 0
        while i < len(data):
            if data[i]["id"] == int(id):
                data[i]["status"] =  "done"
                data[i]["updatedAt"] =  str(datetime.datetime.now())
            i+=1

        with open("Task_Tracker.json", "w") as f:
            json.dump(data, f, indent=4)

    def list_(self):

        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return

        print("Current Tasks : ")
        for task in data:
                    print(task["description"])

    def list_done(self):

        try:

            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return
        
        for x in data:
            if x["status"] == "done":
                print(x)
        
    def list_todo(self):

        try:

            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return
        
        for x in data:
            if x["status"] == "todo":
                print(x)
        
    def list_in_progress(self):
       
        try:
            with open("Task_Tracker.json", "r") as f:
                data = json.load(f)
        except (FileExistsError, json.decoder.JSONDecodeError):
            print("No task file found.")
            return
        
        for x in data:
            if x["status"] == "in-progress":
                print(x)
    

def Task_Cmds(cmds):

    global taskito
    

    if cmds == "add":
        taskito.add()
    elif cmds == "update":
        taskito.update(args[1], args[2:])
    elif cmds == "delete":
        taskito.delete(args[1])
    elif cmds == "mark-in-progress":
        taskito.mark_in_progress(args[1])
    elif cmds == "mark-done":
        taskito.mark_done(args[1])
    elif cmds == "list":
        taskito.list_()
    elif cmds == "list done":
        taskito.list_done()
    elif cmds == "list todo":
        taskito.list_todo()
    elif cmds == "list in-progress":
        taskito.list_in_progress()
    else:
        print(" the cmd that u enter is not available in th ecmds list , please try again")


def join_args(args):
    result = " ".join(args)
    return result




args = sys.argv[1:]
cmds = ""
if args:
    cmds = args[0]
if not args:
    print("please provide a command to execute", file=sys.stderr)
taskito = Task_Tracker(id , join_args(args[1:]), "", "", "")
Task_Cmds(cmds)

# x = [{"id":"1", "name":"salah", "age": 23}, {"id": 2, "name":"simo", "age": 24}]
# print(x[0]["name"])