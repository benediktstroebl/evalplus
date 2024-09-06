

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l2 = []
    l3 = []
    l4 = []
    for k in l:
        if k % 3 == 0:
            l2.append(k)
        elif k % 3 == 1:
            l3.append(k)
        else:
            l4.append(k)
    l3.sort()
    l4.sort()
    l2 = l3 + l4
    for k in l2:
        l.remove(k)
    l = l + l2
    return l

