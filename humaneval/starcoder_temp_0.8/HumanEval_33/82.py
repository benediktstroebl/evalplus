

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l[:]
    l1 = []
    l2 = []
    for i in l:
        if i % 3 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l.clear()
    l1.sort()
    l2.sort()
    l.extend(l1)
    l.extend(l2)
    return l
