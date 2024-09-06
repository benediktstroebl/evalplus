
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    assert x <= y, "x must be smaller than y"
    assert x > 0 and y > 0, "both x and y must be positive numbers"
    # Your code here
    if x%2!= 0:
        x += 1
    return x + (y - x)//2
