
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    
    result = 0 
    for index, value in enumerate(lst):
        if value % 2 == 0:
            if index % 2 == 0:
                result += value
    return result 
