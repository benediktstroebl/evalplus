
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_min, y_min = min(x, y)
    x_max, y_max = max(x, y)
    while x_min <= y_max:
        i = int((x_min + y_max) / 2)
        if x_min * x_min <= (i * i + x_max - x_min):
            x_min = i + 1
        else:
            y_min = i + 1
    return x_min

if __name__ == '__main__':
    x = int(input().strip())
    y = int(input().strip())
    choice = choose_num(x, y)
    if choice == -1:
        print("Invalid input")
    else:
        print(choice)