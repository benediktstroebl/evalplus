
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    while n > 0:
        if lst[n//2] % 2 == 0:
            lst.insert(n//2 + 1, lst.pop(n//2))
            n -= 1
        n //= 2
    return lst
