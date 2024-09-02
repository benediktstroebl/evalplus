
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not isinstance(lst, list) or len(lst) == 0:
        return None
    else:
        return lst[0] + add(lst[1:]) if len(lst) > 1 and lst[0] % 2 == 0 else lst[0]

