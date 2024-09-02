
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([n for i, n in enumerate(lst) if n % 2 == 0 and i % 2 == 1])

