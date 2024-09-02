

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    odd_l = l[1::2]
    odd_l.sort()

    index_l = [i+1 for i in range(0, len(odd_l), 2)]
    index_l.sort()
    index_l = [i for i in index_l]

    if len(index_l) != len(l):
        raise ValueError("sort_even: Not enough elements in l to sort")
    return [ l[i-1] for i in index_l ]
