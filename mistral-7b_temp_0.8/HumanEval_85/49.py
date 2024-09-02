
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return list(filter(lambda x: (x % 2 == 0) and (x % 4 == 3), lst))


