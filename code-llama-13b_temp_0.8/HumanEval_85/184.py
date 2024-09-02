
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    for idx, el in enumerate(lst):
        if idx % 2 == 1 and el % 2 == 0:
            sum += el
    return sum


