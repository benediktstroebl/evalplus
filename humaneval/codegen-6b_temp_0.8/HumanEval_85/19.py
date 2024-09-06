
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    index = 0
    result = 0
    length = len(lst)

    while index < length:
        add = lst[index]
        if add % 2 == 0:
            result = result + add
        index = index + 1

    return result

