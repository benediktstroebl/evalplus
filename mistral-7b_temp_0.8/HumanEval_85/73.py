
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return 0
    else:
        if lst[1] % 2 == 0:
            lst.pop(0)
            lst.append(lst.pop(0))
            return add(lst)
        else:
            return lst[1]
