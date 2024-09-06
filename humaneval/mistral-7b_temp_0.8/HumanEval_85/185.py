
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # TODO: write your own implementation of add

    result = 0
    for i, element in enumerate(lst):
        if element % 2 == 0:
            result += lst[i]
    return result

