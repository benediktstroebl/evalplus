
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    assert lst, "lst can not be empty"
    assert all(type(x) == int for x in lst), "lst must contains only integers"
    assert len(lst) > 1, "lst must have at least 2 elements"
    return sum([lst[x] for x in range(len(lst)) if x % 2 == 1 and lst[x] % 2 == 0])



