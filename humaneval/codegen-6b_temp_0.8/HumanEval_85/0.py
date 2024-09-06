
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return None

    elif len(lst) == 1:
        return lst.pop()

    elif len(lst) == 2:
        if lst[0] % 2 != 0:
            return 0
        return lst.pop()

    else:
        if lst[0] % 2 == 0:
            return add(lst[1:])
        else:
            return 0 + add(lst[1:])


the_list = [4, 2, 6, 7]
