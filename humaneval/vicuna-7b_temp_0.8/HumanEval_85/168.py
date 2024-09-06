
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = sorted(lst)
    if not lst[1:]:
        return lst[0]
    else:
        for i in range(1, len(lst)):
            if not lst[i]:
                return lst[lst[0:i-1].index(lst[0])]
            elif lst[i] % 2 == 0:
                return lst[lst[0:i-1].index(lst[0])] + (lst[i])
            else:
                return lst[lst[0:i-1].index(lst[0])] + (lst[i])
