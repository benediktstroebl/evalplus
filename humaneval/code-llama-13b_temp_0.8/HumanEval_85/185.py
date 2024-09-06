
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0
    
    s = 0
    for i, n in enumerate(lst):
        if n % 2 == 0 and i % 2 == 1:
            s += n
    return s
