
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even = []
    for x in lst:
        if x % 2 == 0:
            even.append(x)
    return even
