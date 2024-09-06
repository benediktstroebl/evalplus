
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [x for x in lst if not x % 2]
    return [lst[0], lst[1], lst[1] % 2]