

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert type(l) == list, "l must be a list"
    l_sorted = l[:]
    for i in range(0, len(l_sorted), 2):
        l_sorted[i] = min(l[i], l[i+1])
        l_sorted[i+1] = max(l[i], l[i+1])
    return l_sorted
