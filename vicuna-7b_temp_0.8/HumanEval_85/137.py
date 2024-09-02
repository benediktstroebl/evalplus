
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    s = 0
    for i in range(len(lst)):
        if (lst[i] % 2 == 0 and lst[i] != 0):
            s += lst[i]
            lst[i] = 0
        else:
            lst[i] += s
            s = 0
    return lst