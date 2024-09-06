

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    assert type(l) == list, "Argument must be a list"
    # base case
    if len(l) == 0:
        return l
    # recursive case
    if l[-1] % 3 == 0:
        return [l[-1]] + sort_third(l[:-1])
    else:
        return [l[-1]] + sort_third(l[:-1]) + l[-1:]
