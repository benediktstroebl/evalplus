

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l1 = []
    for i in l:
        if i % 3 != 0:
            l1.append(i)
    l2 = []
    for j in l:
        if j % 3 == 0:
            l2.append(j)
    l3 = []
    for k in l:
        if k % 3 == 0:
            l3.append(sorted(l2)[l2.index(k)])
    l4 = []
    for m in l:
        if m % 3 != 0:
            l4.append(m)
    return l4 + l3

