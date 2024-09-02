
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if lst[0] % 2 == 0:
        return add(lst[1:])
    if lst[1] % 2 == 0:
        return lst[0] + add(lst[2:])
    return lst[0] + add(lst[2:])
