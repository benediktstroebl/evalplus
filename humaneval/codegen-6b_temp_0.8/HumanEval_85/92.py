
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_len = len(lst)
    #return None if lst_len == 0 else lst[0] + add(lst[2:]) if lst_len > 0 and lst[1] % 2 == 0 else lst[0] + add(lst[2:])
    
    if lst_len == 0:
        return None
    elif lst_len == 1:
        if lst[0] % 2 == 0:
            return lst[0]
        else:
            return None
    elif lst_len > 1 and lst[1] % 2 == 0:
        return lst[0] + add(lst[2:])
    else:
        return lst[0] + add(lst[2:])

