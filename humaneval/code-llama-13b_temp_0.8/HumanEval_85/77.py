
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not isinstance(lst, list):
        raise TypeError("should be a list")
    if len(lst) <= 0:
        raise ValueError("should be non-empty")
    result = 0
    for index, value in enumerate(lst):
        if value % 2 == 0 and index % 2 != 0:
            result += value
    return result
