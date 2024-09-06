
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst)%2:
        return
    if len(lst)<2:
        return lst
    return lst[1::2] + lst[0::2]
