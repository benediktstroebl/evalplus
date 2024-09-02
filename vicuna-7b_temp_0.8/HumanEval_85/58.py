
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = sorted(lst)
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] == lst[i+1]:
                lst.remove(lst[i])
                lst.remove(lst[i+1])
    return lst
