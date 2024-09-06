
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = sorted(lst)
    for i in range(len(lst)):
        if (lst[i] % 2 == 0 and lst[i+1] % 2 != 0):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst