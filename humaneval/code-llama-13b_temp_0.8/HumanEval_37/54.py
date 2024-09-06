

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # first we need to sort l
    l.sort()
    # we also need to get a copy of l, so we can work on that
    l_copy = l[:]
    # now we can iterate through l, if the index is even, we can swap the value of the same index with l_copy
    for i in range(len(l)):
        if i % 2 == 0:
            # we only need to swap if the item at the even index of l is not equal to the value of the same index in l_copy
            if l[i] != l_copy[i]:
                l[i] = l_copy[i]
                l_copy[i] = l[i]
    # now we can return l
    return l

