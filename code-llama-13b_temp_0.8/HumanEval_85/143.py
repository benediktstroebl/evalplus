
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0
    
    val = 0
    for index, item in enumerate(lst):
        if index % 2 == 0 and item % 2 == 0:
            val += item
    return val

