
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if lst == []:
        return 0
    even = sum(lst[::2])
    odd = sum(lst[1::2])
    return even * 2 + odd
