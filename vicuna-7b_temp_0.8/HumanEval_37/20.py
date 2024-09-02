

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # if len(l) == 0 return an empty list
    if len(l) == 0:
        return []
    # if len(l) == 1 return the list as is
    if len(l) == 1:
        return l
    # sort the odd indices
    l_odd = sorted(l[1::2])
    # copy the odd indices to a new list
    l_even = l[1::2]
    # sort the even indices
    l_even.sort()
    # concatenate the two lists
    return l_odd + l_even