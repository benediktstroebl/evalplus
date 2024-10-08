

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if not l:
        return []
    return [l[1]] + sort_even([x for x in l[2:] if x % 2 == 0]) + [l[0]] + sort_even([x for x in l[2:] if x % 2 != 0])

