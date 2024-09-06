
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) > 0:
        lst.append(lst[0] + lst[1] if lst[0] % 2 == 1 else lst[0])
        return add(lst[2:])
    return lst
