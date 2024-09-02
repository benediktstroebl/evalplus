
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    """
    m = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 1:
            m.append(lst[i])
    return m
    """
    m = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            m.append(lst[i])
    return m
