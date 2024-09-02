
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    newlst = []
    for idx, elem in enumerate(lst):
        if (idx + 1) % 2 == 0 and elem % 2 == 0:
            newlst.append(elem)
    return sum(newlst)
