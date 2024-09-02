
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return 0
    
    sum = 0
    for i in range(0, len(lst) - 1, 2):
        sum += lst[i]
    
    return sum
