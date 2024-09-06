

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    if len(l) < 2:
        return l

    # copy list
    l_out = list(l)

    # store even indicies
    evens = [i for i in range(len(l)) if i % 2 == 0]

    # sort even indicies
    for i in range(len(evens)):
        if l[evens[i]] > l[evens[i + 1]]:
            l_out[evens[i]], l_out[evens[i + 1]] = l_out[evens[i + 1]], l_out[evens[i]]

    return l_out

