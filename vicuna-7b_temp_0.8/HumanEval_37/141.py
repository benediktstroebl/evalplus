

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    i = j = l.index(max(l, key=lambda x: x if x % 2 == 0 else float('inf')))
    while j < len(l):
        l[j], l[i] = l[i], l[j]
        i += 1
        j += 1
    return l
