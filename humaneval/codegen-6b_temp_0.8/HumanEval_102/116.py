
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Your code here
    if x > y:
        return -1
    mid = (x+y)//2
    if mid%2 == 0 and (mid <= x or mid >= y):
        return mid
    elif mid%2 == 0 and (mid > x and mid < y):
        return mid
    else:
        return -1
        
