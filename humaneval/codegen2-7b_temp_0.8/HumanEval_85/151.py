
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return
    else:
        for i in range(0,len(lst)):
            if i%2 == 1:
                lst.append(lst[i])
    return
