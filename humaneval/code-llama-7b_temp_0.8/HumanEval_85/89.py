
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # 1. Base Case
    if len(lst) == 1:
        return lst[0]
    # 2. Recursive Step
    if (len(lst) % 2 == 0 and (lst[len(lst) - 1] % 2 == 0)):
        return lst[len(lst) - 1] + add(lst[:-1])
    elif (len(lst) % 2 != 0 and (lst[len(lst) - 1] % 2 != 0)):
        return add(lst[:-1])
    else:
        return add(lst[1:])
