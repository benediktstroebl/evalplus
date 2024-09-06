
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    ans = 0
    for i in range(0,n,2):
        ans+=lst[i]

    return ans
