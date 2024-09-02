

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = []
    for indice in range(len(l)):
        l_copy.append(l[indice])
    # sort l_copy only if it's even
    if (len(l_copy) % 2 == 0):
        l_copy.sort()
    return l_copy

