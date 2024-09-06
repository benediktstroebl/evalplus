
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return
    else:
        res = lst[0]
        for i in range(1, len(lst)):
            if i % 2 == 0 and lst[i] % 2 == 0:
                res = res + lst[i]
            else:
                continue
        return res
