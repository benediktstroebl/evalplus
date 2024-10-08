
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    index = 0
    while index < (len(lst)):
        if index % 2 == 0:
            lst[index] = lst[index] + lst[index]
        index += 1
    return lst
