

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
    i = 0
    j = len(l) - 1
    while j > i:
        if l[j] % 2 != l[i] % 2:
            break
        j, i = i, j - 1
    while j >= i:
        l[j], l[i] = l[i], l[j]
        j -= 2
        i += 2
    return l