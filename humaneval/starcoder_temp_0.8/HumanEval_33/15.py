

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
    for i in l:
        if i % 3 == 0:
            l4.append(i)
        if i % 3 == 1:
            l2.append(i)
        if i % 3 == 2:
            l3.append(i)
    l.clear()
    l.extend(l4)
    l.extend(l2)
    l.extend(l3)
    return l
