
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 2 == 1 and val % 2 == 0:
            total += val
    return total
