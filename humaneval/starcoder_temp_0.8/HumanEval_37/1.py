

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert len(l) >= 1, "List must have at least 1 item in it"
    l_sorted = l
    even_indicies = range(1, len(l), 2)
    for index in even_indicies:
        l_sorted[index], l_sorted[index-1] = l_sorted[index-1], l_sorted[index]
    return l_sorted
