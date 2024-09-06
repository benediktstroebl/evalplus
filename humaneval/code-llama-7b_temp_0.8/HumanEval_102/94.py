
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0:
        even_x = x
    else:
        even_x = x + 1
    if y % 2 == 0:
        even_y = y
    else:
        even_y = y - 1
    if even_x > even_y:
        return -1
    for num in range(even_x, even_y+1, 2):
        if num >= even_x:
            even_x = num
        if num <= even_y:
            even_y = num
    return even_y

