
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0

    result = 0
    for idx in range(1, len(lst), 2):
        result += lst[idx]
    return result

