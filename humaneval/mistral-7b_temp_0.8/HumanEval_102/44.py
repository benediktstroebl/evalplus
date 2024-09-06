
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    if x < y:
        if x % 2 == 0:
            if y % 2 == 0:
                if x > y:
                    print(y)
                else:
                    print(x)
            else:
                if x > y:
                    print(y)
                else:
                    print(x)
        else:
            if y % 2 == 0:
                print(y)
            else:
                print(-1)
    elif x > y:
        if x % 2 == 0:
            if y % 2 == 0:
                print(x)
            else:
                print(y)
        else:
            print(-1)
    else:
        print(-1)

