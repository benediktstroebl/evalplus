

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    r = []
    for i in range(len(l)):
        if i % 2 == 0:
            r.append(l[i])
    r.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = r[0]
            r.pop(0)
    return l

