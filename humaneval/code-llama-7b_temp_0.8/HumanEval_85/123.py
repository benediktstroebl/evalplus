
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    assert lst and isinstance(lst, list), "Invalid input"
    assert all(isinstance(item, int) for item in lst)
    return sum(x for x in lst[1::2] if x % 2 == 0)

