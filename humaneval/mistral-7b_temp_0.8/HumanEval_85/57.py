
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return
    odd = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 0 and i % 2 == 1:
            odd = lst[i] + odd
    return odd
