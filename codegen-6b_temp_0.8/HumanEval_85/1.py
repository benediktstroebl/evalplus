
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    while i < len(lst) - 1:
        if lst[i] % 2 == 0 and lst[i + 1] % 2 == 1:
            lst[i] += lst[i + 1]
            lst.pop(i + 1)
        else:
            i += 1
    return lst[-1] if len(lst) > 0 else None

