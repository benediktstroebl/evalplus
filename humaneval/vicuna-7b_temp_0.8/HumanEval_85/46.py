
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    if n % 2 == 0:
        return lst
    else:
        for i in range(n-1, -1, -1):
            if i % 2 == 0:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                lst.pop(i+1)
        return lst
