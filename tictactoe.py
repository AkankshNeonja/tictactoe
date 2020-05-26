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























