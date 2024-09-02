
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    lst2 = []
    for i in range(n):
        if i % 2 == 1:
            lst2.append(lst[i])
    lst = lst[:n] + [lst2] + lst[n:]
    return lst