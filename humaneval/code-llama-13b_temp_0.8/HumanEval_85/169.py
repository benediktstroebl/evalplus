
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) < 2:
        return 0
    s = 0
    for i in range(1,len(lst), 2):
        s += lst[i]
    return s
