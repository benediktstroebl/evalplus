
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        return lst[1::2] + add(lst[::2])

"""
