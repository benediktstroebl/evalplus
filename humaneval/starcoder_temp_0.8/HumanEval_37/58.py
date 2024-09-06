

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    if len(l) <= 1:
        return l
    l1 = l[::2]
    l2 = sort_even(l[1::2])
    res = [None] * (len(l1) + len(l2))
    for i in range(0, len(l1)):
        res[2*i] = l1[i]
    for i in range(0, len(l2)):
        res[2*i+1] = l2[i]
    return res
