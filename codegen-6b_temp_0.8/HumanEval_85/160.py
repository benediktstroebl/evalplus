
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    res = []
    for item in lst:
        if item % 2 == 0:
            res.insert(0, item)
    return res
