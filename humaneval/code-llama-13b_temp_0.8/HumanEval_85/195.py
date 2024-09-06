
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_ = lst[1::2]
    res = 0
    for i in lst_:
        res += i
    return res
