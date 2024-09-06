

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
        return l
    if len(l) == 1:
        return l
    l1 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
    l1.sort()
    l2 = l1.copy()
    l2.reverse()
    l1 = l1.copy()
    for i in range(len(l)):
        if i % 2 != 0:
            l[i] = l1.pop(0)
        else:
            l[i] = l2.pop(0)
    return l

