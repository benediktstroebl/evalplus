
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    size = len(lst)
    return sum([lst[i] if i % 2 == 0 else 0 for i in range(0, size)])
