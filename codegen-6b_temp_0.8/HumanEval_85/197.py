
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    assert type(lst) == list, "lst must be a list."
    assert len(lst) > 0, "lst must not be empty."
    if len(lst) < 3:
        return 0
    else:
        for i in range(0, len(lst) - 1, 2):
            lst[i] += lst[i + 1]
            lst.pop(i + 1)
        return lst[0]

