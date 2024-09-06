

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
    if len(l) == 2:
        return [l[1], l[0]]

    temp = l[::2]
    temp = sorted(temp)
    for i in range(len(temp)):
        l[i*2] = temp[i]
    return l


