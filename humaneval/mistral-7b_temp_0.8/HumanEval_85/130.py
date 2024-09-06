
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst.insert(0,0)
    lst.pop(1)
    lst.insert(0,0)
    return lst[0]
