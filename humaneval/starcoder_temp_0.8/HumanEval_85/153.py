
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = 0
    for index, i in enumerate(lst):
        if index % 2 == 1 and i % 2 == 0:
            result += i
    return result


