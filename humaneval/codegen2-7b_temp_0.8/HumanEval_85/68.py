
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst=sorted(lst)
    return lst[(lst.index(2)+1)%2]+lst[(lst.index(2)+3)%
