
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 1
    for x in lst:
        if i % 2 == 0:
            lst.append(x)
            i += 1
        i += 1
    return
