
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even = 0
    for i in range(n-1):
        even += lst[i]
    for i in range(n-1, -1, -1):
        lst[i] = 0
        lst[i-1] += lst[i]
    return lst