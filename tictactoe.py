print("---------")
print("| {0} {1} {2} |".format(" ", " ", " "))
print("| {0} {1} {2} |".format(" ", " ", " "))
print("| {0} {1} {2} |".format(" ", " ", " "))
print("---------")


dict_inp = {('1', '3'): " ",
            ('2', '3'): " ",
            ('3', '3'): " ",
            ('1', '2'): " ",
            ('2', '2'): " ",
            ('3', '2'): " ",
            ('1', '1'): " ",
            ('2', '1'): " ",
            ('3', '1'): " "}


def check_win(dict_inp):
    if (dict_inp[('1','3')] == dict_inp[('2','3')] == dict_inp[('3','3')]) and dict_inp[('1','3')] != " ":
        return True
    if (dict_inp[('1','2')] == dict_inp[('2','2')] == dict_inp[('3','2')]) and dict_inp[('1','2')] != " ":
        return True
    if (dict_inp[('1','1')] == dict_inp[('2','1')] == dict_inp[('3','1')]) and dict_inp[('1','1')] != " ":
        return True
    if (dict_inp[('1','3')] == dict_inp[('1','2')] == dict_inp[('1','1')]) and dict_inp[('1','3')] != " ":
        return True
    if (dict_inp[('2','3')] == dict_inp[('2','2')] == dict_inp[('2','1')]) and dict_inp[('2','3')] != " ":
        return True
    if (dict_inp[('3','3')] == dict_inp[('3','2')] == dict_inp[('3','1')]) and dict_inp[('3','3')] != " ":
        return True
    if (dict_inp[('1','3')] == dict_inp[('2','2')] == dict_inp[('3','1')]) and dict_inp[('1','3')] != " ":
        return True
    if (dict_inp[('1','1')] == dict_inp[('2','2')] == dict_inp[('3','3')]) and dict_inp[('1','1')] != " ":
        return True
    else:
        return False


def display_output(dict_inp):
    print("---------")
    print("| {0} {1} {2} |".format(dict_inp[("1","3")], dict_inp[("2","3")], dict_inp[("3","3")]))
    print("| {0} {1} {2} |".format(dict_inp[("1","2")], dict_inp[("2","2")], dict_inp[("3","2")]))
    print("| {0} {1} {2} |".format(dict_inp[("1","1")], dict_inp[("2","1")], dict_inp[("3","1")]))
    print("---------")


while True:
    move_count = 1
    inp_coord = tuple(list(input().split(" ")))
    if inp_coord in dict_inp:
        if move_count % 2 == 1:
            if dict_inp[inp_coord] != "X" and dict_inp[inp_coord] != "O":
                dict_inp[inp_coord] = "X"
                move_count += 1
                display_output(dict_inp)
                if check_win(dict_inp):
                    print("X wins")
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            if dict_inp[inp_coord] != "X" and dict_inp[inp_coord] != "O":
                dict_inp[inp_coord] = "O"
                move_count += 1
                display_output(dict_inp)
                if check_win(dict_inp):
                    print("O wins")
                    break
            else:
                print("This cell is occupied! Choose another one!")
    else:
        if int(inp_coord[0]) > 3 and int(inp_coord[1]) > 3 and int(inp_coord[0]) < 1 and int(inp_coord[1]) < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")




"""def count_x_o(inp):
    cnt_X = 0
    cnt_O = 0
    for i in inp:
        if i == "X":
            cnt_X += 1
        elif i == "O":
            cnt_O += 1
        else:
            pass
    return abs(cnt_X - cnt_O)


def count_empty(inp):
    cnt_emp = 0
    for i in inp:
        if i == "_":
            cnt_emp += 1
        else:
            pass
    return cnt_emp


def winner(inp):
    if count_x_o(inp) < 2 and check_win(inp) == 1:
        if inp[0] == inp[1] == inp[2]:
            return inp[0] + " wins"
        elif inp[3] == inp[4] == inp[5]:
            return inp[3] + " wins"
        elif inp[6] == inp[7] == inp[8]:
            return inp[6] + " wins"
        elif inp[0] == inp[4] == inp[8]:
            return inp[0] + " wins"
        elif inp[2] == inp[4] == inp[6]:
            return inp[2] + " wins"
        elif inp[0] == inp[3] == inp[6]:
            return inp[0] + " wins"
        elif inp[1] == inp[4] == inp[7]:
            return inp[1] + " wins"
        elif inp[2] == inp[5] == inp[8]:
            return inp[2] + " wins"
        else:
            return "Game not finished"
    elif count_x_o(inp) >= 2:
        return "Impossible"
    elif check_win(inp) > 1:
        return "Impossible"
    else:
        if count_empty(inp_str) > 0:
            return "Game not finished"
        else:
            return "Draw"

while True:
    pos_inp = tuple(list(input().split(" ")))
    if pos_inp in dict_inp:
        if dict_inp[pos_inp] != "X" and dict_inp[pos_inp] != "O"  :
            dict_inp[pos_inp] = "X"
            check_win(dict_inp)
        else:
            print("This cell is occupied! Choose another one!")
    else:
        if int(pos_inp[0]) > 3 and int(pos_inp[1]) > 3 and int(pos_inp[0]) < 1 and int(pos_inp[1]) < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
"""




















