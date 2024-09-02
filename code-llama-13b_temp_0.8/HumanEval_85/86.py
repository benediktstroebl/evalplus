
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # END OF CONTEXT
    res = 0
    for idx, elem in enumerate(lst):
        if idx % 2 == 0 and elem % 2 == 0:
            res += elem
    return res
    # END OF SOLUTION
