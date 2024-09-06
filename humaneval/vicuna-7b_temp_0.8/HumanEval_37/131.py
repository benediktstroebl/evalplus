

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    l_copy = l[:]
    i = 0
    for j in range(n // 2):
        l_copy[2 * j] = l_copy[2 * j] if l_copy[2 * j] <= l_copy[2 * j + 1] else l_copy[2 * j + 1]
    return l_copy