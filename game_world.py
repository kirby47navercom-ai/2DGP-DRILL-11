world = [[],[],[]]

def add_object(o,depth=0):
    global world
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    else:
        print("ㅇㅅㅇ 없어용:")

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()