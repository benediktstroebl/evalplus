
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = 0
    for i in lst:
        if i%2 == 0 and i%4 == 1:
            n = n+i
    return n


