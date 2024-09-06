
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = lst[:]
    if len(lst) > 1:
        for i in range(1, len(lst)):
            if (lst[i] % 2 == 0) and (lst[i-1] % 2 == 1):
                lst[i], lst[i-1] = lst[i-1], lst[i]
        return lst
    else:
        return lst

lst = [2, 1, 6, 7, 4]
print(add(lst))
