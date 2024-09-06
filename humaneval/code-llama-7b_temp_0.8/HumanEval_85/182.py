
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if type(lst) != list:
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("Input must be non-empty")
    if len(lst) % 2 != 0:
        raise ValueError("Input length must be even")
    if len(lst) == 2:
        return lst[0] + lst[1]
    return lst[1] + add(lst[3:])
