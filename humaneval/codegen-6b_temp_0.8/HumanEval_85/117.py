
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst or type(lst) != list or len(lst) == 1:
        return None

    return sum(lst[:len(lst)//2])

