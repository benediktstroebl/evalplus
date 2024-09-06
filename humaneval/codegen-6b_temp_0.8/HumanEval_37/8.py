

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_1 = l[::2]
    l_2 = sorted(l[1::2])
    i = 0
    l2 = []
    while i < len(l_2):
        l2 = l2 + [l_1[i]] + [l_2[i]]
        i = i + 1
    return l2
