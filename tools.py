from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS=[
    {
        "type":"function",
        "name":"get_current_time",
        "description":"This helps to get the current date and time as a formatted string of any city.",
        "parameters":{
            "type":"object",
            "properties":{
            },
        }
    }
]