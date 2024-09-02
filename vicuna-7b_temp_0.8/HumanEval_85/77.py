
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        x = 0
        for i in range(len(lst)):
            if i % 2 == 1:
                x = lst[i]
                lst[i] = lst[len(lst)-lst.index(lst[-1])-1]
                lst = lst[:lst.index(lst[-1])] + [x] + lst[lst.index(lst[-1]):]
        return lst
