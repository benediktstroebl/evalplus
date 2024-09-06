
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    index = 1
    while index < len(lst):
        if lst[index] % 2 == 0:
            lst[index - 1] += lst[index]
        index += 2
    return lst
