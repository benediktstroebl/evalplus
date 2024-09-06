
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0
    else:
        if lst[0] % 2 == 0 and len(lst) == 1:
            return lst[0]
        elif lst[0] % 2 != 0 and len(lst) == 1:
            return 0
        else:
            return lst[0] + add(lst[2:])
