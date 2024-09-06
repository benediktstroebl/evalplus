
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = list(filter(lambda x: x % 2 == 1, lst))
    return [x for x in lst for _ in range(2)]

