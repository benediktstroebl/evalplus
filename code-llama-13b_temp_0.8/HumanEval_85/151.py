
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if len(lst) == 0:
        raise ValueError('lst must be a non-empty list.')
    
    if len(lst) == 1:
        return lst[0]
    
    idx = 1
    total = 0
    
    while idx < len(lst):
        if lst[idx] % 2 == 0:
            total += lst[idx]
        idx += 2
    
    return total
