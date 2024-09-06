
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if len(lst) > 0:
        result = 0
        for i, val in enumerate(lst):
            if val % 2 == 0 and i % 2 == 1:
                result += val
        return result
    else:
        return 0
