
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        raise ValueError("empty list")
    
    sum = 0
    for i in range(1, len(lst)):
        if lst[i] % 2 == 0:
            sum += lst[i]
    
    return sum
