import json 
import sys
import urllib.request

def join_args(args):
    result = ''.join(args)
    return result

if len(sys.argv) < 2:
    print("please provide a Username to execute the programe;", file=sys.stderr)

Username = sys.argv[1]

url = f"https://api.github.com/users/{Username}/events"


with urllib.request.urlopen(url) as response:
   data = response.read().decode()


activity = json.loads(data)

print(activity)