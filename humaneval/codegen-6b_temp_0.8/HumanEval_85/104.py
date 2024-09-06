
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Index out of range
    if len(lst) > 0:
        if lst[0] % 2 == 0:
            return add(lst[1:])
        else:
            return lst[0] + add(lst[1:])
    else:
        return 0

