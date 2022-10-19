import random as r

board = [["⚪", "⚪", "⚪"], ["⚪", "⚪", "⚪"], ["⚪", "⚪", "⚪"]]
current_mine = "🟢"
last_mine = "🔴"
lastpos = None
currentpos = []
ship_pos = [r.randint(0, 2), r.randint(0, 2)]

def print_board():
    for row in board:
        print(" ".join(row))

print_board()

while True:
    print("It's your turn")
    x = int(input("Enter the x coordinate: "))
    while x < 0 or x > 3:
        x = int(input("Enter valid x coordinate:"))
    y = int(input("Enter the y coordinate: "))
    
    while y < 0 or y > 3:
        y = int(input("Enter valid y coordinate:"))
    board[lastpos[0] - 1][lastpos[1] - 1] = "⚪"
    lastpos = currentpos
    currentpos[0], currentpos[1] = x, y
    board[x - 1][y - 1] = current_mine
    board[lastpos[0] - 1][lastpos[1] - 1] = last_mine
    if currentpos == ship_pos:
        print("You landed on the ship!")
        #you land on the ship
        m = r.randint(-1, 1)
        while (m == 0) and not (ship_pos[1] + m > 2 or ship_pos[1] < 0):
            m = r.randint(-1, 1)
        if r.randint(0, 1) > 0:
            #horizontal movment
            ship_pos[1] += m
        else:
            ship_pos[0] += m
        if ship_pos[0] + 1 == lastpos[0] and ship_pos[1] + 1 == lastpos[1]:
            print("You Win!")
        else:
            print("You Lose! Seriously, a virtual ship beat you?")
    print_board()