
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    b = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            b += lst[i]
            if i % 2 == 0:
                lst[i] = b
    return b
