
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    result = -1
    while result < x or result > y:
        result = eval(input("Enter a number between " + str(x) + " and " + str(y) + ": "))
        if result < x or result > y:
            print("Number must be between " + str(x) + " and " + str(y) + "!")
    if result % 2 == 0:
        return result
    else:
        return -1
