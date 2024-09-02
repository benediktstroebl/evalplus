

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = l.copy()
    i = 1
    while i < len(l_copy):
        if i % 2 == 1:
            l[i], l[i-1] = l[i-1], l[i]
        i += 1
    return l
