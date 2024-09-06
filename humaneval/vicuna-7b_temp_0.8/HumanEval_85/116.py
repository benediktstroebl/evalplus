
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    while n > 0:
        if (lst[n-1] % 2 == 0):
            lst[n-1], lst[n] = lst[n], lst[n-1]
            n -= 1
    return lst

