

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_new = l[:]
    l_even = l[::2]
    l_odd = l[1::2]
    for i in range(len(l_even)):
        l_new[2 * i] = min(l_odd)
        l_odd.remove(min(l_odd))
    return l_new

