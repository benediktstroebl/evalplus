
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return
    i = 0
    while i < len(lst):
        if i%2 == 0:
            i += 1
        else:
            lst[i] += lst[i-1]
            i += 2
    return lst[-1]
