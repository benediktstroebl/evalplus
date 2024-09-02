
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Step 1: check if x and y are positive
    if x <= 0 or y <= 0:
        return -1

    # Step 2: if x > y then switch them
    if x > y:
        x, y = y, x
    
    # Step 3: check if there's a number that is both even and in the range [x, y]
    for num in range(x, y + 1, 2):
        return num

    # Step 4: if there's no such number, return -1
    return -1

