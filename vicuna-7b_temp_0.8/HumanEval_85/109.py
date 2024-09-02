
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    for i in range(n-1, -1, -1):
        if lst[i] % 2 == 0:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
