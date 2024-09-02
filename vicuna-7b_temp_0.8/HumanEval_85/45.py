
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) < 2:
        return lst
    even = [x for x in lst if x % 2 == 0]
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst