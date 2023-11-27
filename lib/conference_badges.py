def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges =["Hello, my name is "+name+"." for name in names] 
    
    return badges

def assign_rooms(names):
    rooms = 1
    room_assignments = []

    for name in names:
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {rooms}!")
        rooms += 1

    return room_assignments

def printer(names):
    for badge_message in batch_badge_creator(names):
        print(badge_message)

    for room_assignment in assign_rooms(names):
        print(room_assignment)
