
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    lst = list(filter(lambda x: x % 2 == 0, lst))
    for i in range(len(lst)):
        lst[i] += lst[i-1] if i % 2 == 1 else 0
    return lst[-1]

