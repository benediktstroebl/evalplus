

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """ O(n log n) solution """
    # l_sorted = sorted(l[1::2])
    # l[1::2] = l_sorted
    # return l

    """ O(n) solution """
    if len(l) == 0 or len(l) == 1:
        return l

    odd_sorted = _sort_odd(l[1::2])
    even_sorted = _sort_even(l[0::2])
    l_sorted = []
    for odd, even in zip(odd_sorted, even_sorted):
        l_sorted.append(even)
        l_sorted.append(odd)
    return l_sorted
