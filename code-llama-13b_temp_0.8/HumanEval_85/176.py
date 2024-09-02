
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0
    total = 0
    for i, val in enumerate(lst):
        if i % 2 == 1 and val % 2 == 0:
            total += val
    return total

