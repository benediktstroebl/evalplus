
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    s = 0
    for e in lst:
        if (i % 2 == 1) and (e % 2 == 0):
            s += e
        i += 1
    return s

