import random
import time

cart_mest = ["зал", "коридор", "управление"]
player_map = {"зеленый": "зал", "красный": "зал", "черный": "зал"}
player = {"зеленый": True, "красный": True, "черный": True}
is_hode_bot = False
is_hode = True
is_kill = False
is_fuck = False
dead = []

def clr():
    for i in range(60):
        print()
        
def cart():
    pl_zl = []
    pl_kr = []
    pl_yp = []
    for i, v in player_map.items():
        if player[i] == True:
            if v == "зал":
                pl_zl.append(i)
            elif v == "коридор":
                pl_kr.append(i)
            elif v == "управление":
                pl_yp.append(i)
                
    for i, v in player_map.items():
        if player[i] == False:
            if v == "зал":
                pl_zl.append(f"!труп: {i}!")
            elif v == "коридор":
                pl_kr.append(f"!труп: {i}!")
            elif v == "управление":
                pl_yp.append("труп: {i}!")
    
    clr()
    print(f" зал({', '.join(pl_zl)}) - коридор({', '.join(pl_kr)}) - управление({', '.join(pl_yp)})")
    
def next():
    global player_map
    Q = True
    Q_1 = True
    Q_2 = True
    
    if is_hode == True:
        if player_map["красный"] == cart_mest[0]:
            while Q:
                clr()
                print("куда вы хотите пойти?")
                print("1. коридор")
                print("2. отмена ")
                req_next = input("> ")
                if req_next == "1":
                    Q = False
                    del player_map["красный"]
                    player_map["красный"] = cart_mest[1]
#                print(player_map)
                elif req_next == "2":
                    Q = False
                
        elif player_map["красный"] == cart_mest[1]:
            while Q_1:
                clr()
                print("куда вы хотите пойти?")
                print("1. зал")
                print("2. управление")
                print("3. отмена")
                req_next = input("> ")
                if req_next == "1":
                    Q_1 = False
                    del player_map["красный"]
                    player_map["красный"] = cart_mest[0]
                    break
#                print(player_map)
                elif req_next == "2":
                    Q_1 = False
                    del player_map["красный"]
                    player_map["красный"] = cart_mest[2]
                    break
#                print(player_map)
                elif req_next == "3":
                    Q_1 = False
            
        if player_map["красный"] == cart_mest[2]:
            while Q_2:
                clr()
                print("куда вы хотите пойти?")
                print("1. коридор")
                print("2. отмена ")
                req_next = input("> ")
                if req_next == "1":
                    Q_2 = False
                    del player_map["красный"]
                    player_map["красный"] = cart_mest[1]
                    print(player_map)
                elif req_next == "2":
                    Q_2 = False
               
        
def npc_logic():
    global player_map
    global dead
    global is_fuck
    hode_bot = False
    hode_bot_2 = False
    
    for i, v in player.items():
        if v == False:
            dead.append(i)
    
    if player["зеленый"] == True:
        
        
            
        if player_map["зеленый"] == cart_mest[0]:
            bot_hode = random.randint(0, 1)
            if bot_hode == 1:
                del player_map["зеленый"]
                player_map["зеленый"] = cart_mest[1]
                hode_bot = True
            elif bot_hode == 0:
                hode_bot = True
            
        elif player_map["зеленый"] == cart_mest[1]:
            bot_hode = random.randint(0, 2)
            if bot_hode == 1:
                del player_map["зеленый"]
                player_map["зеленый"] = cart_mest[0]
                hode_bot = True
            elif bot_hode == 2:
                del player_map["зеленый"]
                player_map["зеленый"] = cart_mest[2]
                hode_bot = True
            elif bot_hode == 0:
                hode_bot = True
            
            
        if player_map["зеленый"] == cart_mest[2]:
            bot_hode = random.randint(0, 1)
            if bot_hode == 1:
                del player_map["зеленый"]
                player_map["зеленый"] = cart_mest[1]
                hode_bot = True
            elif bot_hode == 0:
                hode_bot = True
            
    if player["черный"] == True:
            
        if player_map["черный"] == cart_mest[0]:
            bot_hode_ = random.randint(0, 1)
            if bot_hode_ == 1:
                del player_map["черный"]
                player_map["черный"] = cart_mest[1]
                hode_bot_2 = True
            elif bot_hode_ == 0:
                hode_bot_2 = True
            
        elif player_map["черный"] == cart_mest[1]:
            bot_hode_ = random.randint(0, 2)
            if bot_hode_ == 1:
                del player_map["черный"]
                player_map["черный"] = cart_mest[0]
                hode_bot_2 = True
            elif bot_hode_ == 2:
                del player_map["черный"]
                player_map["черный"] = cart_mest[2]
                hode_bot_2 = True
            elif bot_hode_ == 0:
                hode_bot_2 = True
            
        elif player_map["черный"] == cart_mest[2]:
            bot_hode_ = random.randint(0, 1)
            if bot_hode_ == 1:
                del player_map["черный"]
                player_map["черный"] = cart_mest[1]
                hode_bot_2 = True
            elif bot_hode_ == 0:
                hode_bot_2 = True
    

def kill_npc(reqst):
    global player
    global is_kill
    global is_fuck
    Q1 = True
#    Q2 = True
    is_kill_s = []
    NOTE = []
    num_note = 0
    num_kill = 0

                
    for i, v in player_map.items():
        if v == player_map["красный"]:
            is_kill_s.append(i)
            num_kill = num_kill + 1

    for i, v in player.items():
        if v == False:
            NOTE.append(i)
            num_note = num_note + 1
                
    if num_note == 1:
        is_kill_s.remove(NOTE[0])
        num_kill = num_kill - num_note
    

    is_kill_s.remove("красный")
    num_kill = num_kill - 1
    is_kill = True
    if num_kill == 0:
        is_kill = False
    
    if reqst == True:
        if num_kill == 1:
            while Q1:
                clr()
                print(f"1. {is_kill_s[0]} ")
                print("2. отмена")
                req_kill = input("> ")
                if req_kill == "1":
                    player[is_kill_s[0]] = False
                    Q1 = False
                elif req_kill == "2":
                    Q1 = False
                
        elif num_kill == 2:
            while Q1:
                clr()
                print(f"1. {is_kill_s[0]}")
                print(f"2. {is_kill_s[1]}")
                print("3. отмена")
                req_kill = input("> ")
                if req_kill == "1":
                    player[is_kill_s[0]] = False
                    is_fuck = True
                    Q1 = False
                elif req_kill == "2":
                    player[is_kill_s[1]] = False
                    is_fuck = True
                    Q1 = False
                elif req_kill == "3":
                    Q1 = False
    

    

EZ = True       
while EZ:
    kill_npc(False)
    if "зеленый" in dead and "черный" in dead:
        clr()
        print("вы выйграли!")
        break

    elif is_fuck:
        clr()
        EZ = False
        print("вы проиграли!")
        break
    if EZ == False:
        break
    clr()
    cart()
    print(" DEMO: дерьмовая игра!!! ")
    print()
    print("1. выйти")
    print("2. походить")
    if is_kill:
        print("3. убить")
    req = input("> ")
    if req == "2":
        next()
        npc_logic()
    elif req == "1":
        EZ = False
    elif req == "3" and is_kill:
            kill_npc(True)
            npc_logic()
    
   

  

        
    
    
    
            
