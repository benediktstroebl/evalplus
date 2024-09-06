
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return
    if lst[0] % 2 == 0:
        total = lst[0]
    else:
        total = 0
    for i in range(1, len(lst), 2):
        total += lst[i]
    return total
