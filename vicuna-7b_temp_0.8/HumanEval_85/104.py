
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = 0
    for i in range(len(lst)-1):
        if (lst[i] % 2) == 0:
            even += lst[i]
        else:
            lst[i] = even
            even = lst[i]
    return lst
