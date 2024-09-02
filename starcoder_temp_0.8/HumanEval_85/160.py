
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Your code here
    n = len(lst)
    k = 0
    for i in range(n):
        if (lst[i] % 2 == 0 and i % 2 == 1):
            k = k + lst[i]
    return k
