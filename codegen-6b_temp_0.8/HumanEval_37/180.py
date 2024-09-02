

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert isinstance(l, list)
    assert len(l) >= 1
    for i in range(0, len(l)):
        assert isinstance(l[i], int)
    # make a copy of l so I don't mangle it
    l_copy = l[:]
    # l_copy.sort()
    l_copy = sorted(l_copy)
    # copy the even items to start of l_copy
    for i in range(0, len(l_copy), 2):
        l[i] = l_copy[i]
    # copy the odd items to end of l
    for i in range(1, len(l_copy), 2):
        l[i] = l_copy[i]
    return l

