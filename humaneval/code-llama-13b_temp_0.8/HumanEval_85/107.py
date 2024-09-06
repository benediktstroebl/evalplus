
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    _sum = 0
    for idx in range(len(lst)):
        if idx % 2 == 0 and lst[idx] % 2 == 0:
            _sum += lst[idx]
    return _sum
