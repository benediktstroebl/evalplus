
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst2 = lst[::2]
    lst2.extend(lst[1::2])
    return sum(lst2)

