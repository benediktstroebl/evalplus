

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    if l[0] % 2 == 0:
        if l[1] < l[0]:
            return [l[1]] + sort_even(l[2:])
        else:
            return [l[0]] + sort_even(l[2:])
    else:
        if l[1] < l[0]:
            return [l[0]] + sort_even(l[2:])
        else:
            return [l[1]] + sort_even(l[2:])
    
