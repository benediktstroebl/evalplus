
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    res = 0
    while i < len(lst):
        if lst[i]%2 == 0:
            res += lst[i]
        i += 2
    return res
