class Player:
    def __init__(self, hp=100, basedamage=10, stamina=100, hasweapon=False,):
        self.hp = int(hp)
        self.basedamage = int(basedamage)
        self.stamina = int(stamina)
        self.hasweapon = bool(hasweapon)


class Items:
    def __init__(self, weapondamage=100, durability=10):
        self.weapondamage = int(weapondamage)
        self.durability = int(durability)


def showplayerstatus():
    return "This is your current Status:", "Health", player.hp, \
           "Damage:", player.basedamage, "Stamina:", player.stamina, \
           "Do I have a weapon?:", player.hasweapon

def showdirections():
    if currentRoom == 1:
        return "From here you can go: right"
    elif currentRoom == 2:
        return "From here you can go: right or back"
    elif currentRoom == 3:
        return "From here you can go: back"
def getitem(rustySword):
    if rustySword in rooms[currentRoom].values():
        if move[0] == "get":
            if player.hasweapon is True:
                print("you already have a weapon! If you want a new one, you first need to drop your current one!")
            if player.hasweapon is False:
                player.hasweapon = True
                print("nice you got it")
                player.basedamage = (int(player.basedamage) + int(rustySword.weapondamage))

    elif rustySword not in rooms[currentRoom].values():
        print("Nothing to pick up here")

player = Player()


rustySword = Items()
rustySwordDetails = ["Name: A Rusty Sword", "Damage:", rustySword.weapondamage, "Durability:", rustySword.durability]
# type(playerStats)
attacks = {}
currentRoom = 1
# print(type(playerStats))

rooms = {1: {"name": "living Room",
             "right": 2},
         2: {"name": "Hall",
             "back": 1,
             "right": 3},
         3: {"name": "Bedroom",
             "back": 2,
             "item": rustySword}
         }
print("you are in room: " + str(currentRoom))
print("this is the " + rooms[currentRoom]["name"])
print(showplayerstatus())
print("You can check your status by typing: \"status\" ")
print(showdirections())
damage = 0

while True:
        move = input(">\n").lower().split()

        if move[0] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[0]]
            print("You have entered this room: ", rooms[currentRoom]["name"])
            # print(showplayerstatus())
            print(showdirections())
            if rooms[currentRoom].__contains__("item"):
                print("This room has an item in it: ", rustySwordDetails)
                print("if you want to pick it type: get")

        elif move[0] == "status":
            print(showplayerstatus())
        elif move[0] == "get":
            getitem(rustySword)
        else:
            print("invalid command")