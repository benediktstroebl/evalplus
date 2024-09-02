
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if type(lst) != list:
        return "lst must be a list"
    elif not lst:
        return "lst cannot be empty"
    else:
        return sum(l for l in lst[::2] if l % 2 == 0)
