
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return lst
    for i in range(len(lst)):
        if i % 2 == 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

lst = [2, 4, 1, 3, 5, 2, 6, 7, 1, 3, 4, 5, 6, 7, 1, 5, 3]
