

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
    l2 = []
    l3 = []
    for i in l:
        if i%3 == 0:
            l3.append(i)
        elif i%3 == 1:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.sort()
    l3.sort()
    l = []
    for i in l1:
        l.append(i)
    for i in l2:
        l.append(i)
    for i in l3:
        l.append(i)
    return l
