
def pick(filename, data):
    import pickle

    with open(filename, "wb") as f:
        pickle.dump(data, f)


def unpick(filename):
    import pickle

    with open(filename, "rb") as f:
        return pickle.load(f)


def get_time() -> str:
    import datetime

    return "from_system||"+str({"time": datetime.datetime.now().strftime("%H:%M:%S %d.%m.%Y")})


def create_dir(name: str) -> str:
    import os

    try:
        os.mkdir(name)
        return "from_system||" + "Directory " + name + " created"
    except:
        return "from_system||" + "Directory " + name + " already exists"


def remove_dir(name: str) -> str:
    import os

    try:
        os.rmdir(name)
        return "from_system||" + "Directory " + name + " removed"
    except:
        return "from_system||" + "Directory " + name + " does not exist"


def get_memories() -> str:
    import os

    if "memories" not in os.listdir():
        pick("memories", [])

    return "from_system||" + str(unpick("memories"))


def add_memory(text: str) -> str:
    import os
    try:
        if "memories" not in os.listdir():
            pick("memories", [])
        memories = unpick("memories")
        memories.append(text)
        pick("memories", memories)
        return "from_system||" + "Memory added"
    except Exception as e:
        return "from_system||" + "Memory not added. Error: " + str(e)


