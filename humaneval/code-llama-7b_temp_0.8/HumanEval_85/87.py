
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = 0

    for i in range(0, len(lst), 2):
        if (i + 1) < len(lst):
            if (lst[i] % 2) != 0:
                result += lst[i + 1]

    return result
