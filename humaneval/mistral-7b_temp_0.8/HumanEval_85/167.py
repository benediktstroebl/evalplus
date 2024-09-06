
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = list(filter(lambda x: x % 2 == 0, lst))
    lst = list(filter(lambda x: x % 2 != 0, lst))
    sum = 0
    for i in range(0, len(lst)):
        sum += lst[i]
    return sum

