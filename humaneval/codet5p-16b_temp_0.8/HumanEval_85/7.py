
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    for i, j in enumerate(lst):
        if j % 2 == 1 and i % 2 == 1:
            lst[i] += 2
    return lst
