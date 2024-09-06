
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x%2==0 and x<y:
        return x
    elif x%2==0 and x>y:
        return -1
    elif x%2!=0 and x<y:
        r=x+1
        while True:
            if r%2==0 and r<y:
                return r
            else:
                r+=1
    elif x%2!=0 and x>y:
        r=x+1
        while True:
            if r%2==0 and r>y:
                return r
            else:
                r+=1
    else:
        return -1

