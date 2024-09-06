
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    for i, v in enumerate(lst):
        if i % 2 == 1:
            if v % 2 == 0:
                sum += v
    return sum

