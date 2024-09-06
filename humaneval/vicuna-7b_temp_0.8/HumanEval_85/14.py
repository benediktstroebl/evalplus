
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i, j = 0, len(lst)-1
    while i < j:
        if (lst[i] % 2 == 0) and (lst[j] % 2 != 0):
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    return lst

