

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    assert len(l) <= 20, "List should have a length in the range [0,20]"
    l_copy = l[:]
    l.sort()
    for i in range(0, len(l)):
        if i % 3 != 0:
            l[i] = l_copy[i]
    return l

