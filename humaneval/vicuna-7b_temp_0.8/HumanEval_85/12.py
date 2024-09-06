
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = sorted(lst)
    if not lst[0] % 2 == 0:
        lst = lst[1:] + lst
    return lst
