
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    ret = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if lst[i] % 4 == 2:
                ret += lst[i]
    return ret
