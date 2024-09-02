
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if the input values are positive
    if x < 0 or y < 0:
        return -1

    # Check if x and y are equal
    if x == y:
        return x

    # Check if x is bigger than y
    if x > y:
        return x

    # Check if y is bigger than x
    if y > x:
        return y

    # If x and y are equal or x is bigger than y, we can return the biggest 
    # even integer in the range [x, y]
    if x % 2 == 0 and y % 2 == 0:
        return max(x, y)

    # If there's no such even integer in the range [x, y], we return -1
    else:
        return -1
