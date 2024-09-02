
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # validations
    if not isinstance(lst, list):
        return 'Argument should be of type list'

    if len(lst) == 0:
        return 'Argument should be a non-empty list'

    result = 0
    for i, x in enumerate(lst):
        if i % 2 == 0 and x % 2 == 0:
            result += x
    return result
