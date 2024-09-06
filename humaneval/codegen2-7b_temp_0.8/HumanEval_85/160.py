
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst or len(lst) == 1:
        return lst
    else:
        return lst[0] + add(lst[1:])
