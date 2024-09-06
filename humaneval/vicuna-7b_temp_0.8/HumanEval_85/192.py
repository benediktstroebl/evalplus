
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    i = 0
    for j in range(n-1):
        if lst[j] % 2 == 0 and lst[j+1] % 2 == 1:
            lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst