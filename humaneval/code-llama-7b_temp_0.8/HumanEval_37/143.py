

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = sorted([i for i in l if i % 2 == 0])
    l3 = []
    if len(l2) > 0:
        for i in l:
            if i % 2 == 0:
                l3.append(l2.pop(0))
            else:
                l3.append(i)
    else:
        for i in l:
            if i % 2 == 0:
                l3.append(i)
            else:
                l3.append(l2.pop(0))
    return l3
