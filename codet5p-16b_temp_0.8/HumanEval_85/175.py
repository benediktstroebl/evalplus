
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    x = lst[::2] # ['4', '2', '6', '7']
    y = lst[1::2] # ['2', '7']
    return sum(x) - sum(y)
