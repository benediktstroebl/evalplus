
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if len(lst)<=1:
        return lst
    lst1=lst[0::2]
    lst2=lst[1::2]
    return add(lst1)+add(lst2)
