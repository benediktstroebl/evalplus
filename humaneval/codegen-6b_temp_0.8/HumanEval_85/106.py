
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = -1
    for x in lst:
        i = i + 1
        if x % 2 == 0:
            lst[i] = lst[i] + x
    return lst

