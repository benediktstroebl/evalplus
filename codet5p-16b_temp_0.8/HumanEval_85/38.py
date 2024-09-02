
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    result = 0
    for index in range(1, len(lst), 2):
        result += lst[index]
    return result
