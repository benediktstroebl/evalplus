

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = l[:]
    l_even = l[::2]
    l_odd = l_copy[::2]
    if len(l_even) > 0:
        l_even = sorted(l_even)
    return l_odd + l_even


