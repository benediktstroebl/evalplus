

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # initialize a list to hold our output
    lp = [None for _ in range(len(l))]

    # loop through l and copy the items to lp
    for i in range(len(l)):
        if i % 2 == 0:
            # even index
            lp[i] = l[i]
        else:
            # odd index, copy but sort
            lp[i] = sorted(l)[i]
    return lp

    # an alternate solution, that uses zip and itertools
    # from itertools import zip_longest
    # return [sorted(x)[i] if i % 2 == 0 else x[i] for i, x in enumerate(zip_longest(l, l))]
