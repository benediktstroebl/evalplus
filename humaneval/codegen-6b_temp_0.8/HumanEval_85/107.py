
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    shouldAdd = False
    for i in lst:
        if i % 2 == 0:
            shouldAdd = True
        else:
            if shouldAdd:
                return i


