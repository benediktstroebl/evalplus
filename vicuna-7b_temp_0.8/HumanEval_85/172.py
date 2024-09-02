
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return None
    i = 0
    while i < len(lst) - 1:
        if lst[i] % 2 == 0:
            lst.insert(i + 1, lst.pop(i))
            i += 1
        i += 1
    return lst