
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = 0
    for i, item in enumerate(lst):
        if i % 2!= 0 and item % 2 == 0:
            result += item
    return result
