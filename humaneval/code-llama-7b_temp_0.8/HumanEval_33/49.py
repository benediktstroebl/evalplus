

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    a = []
    b = []
    for i in range(len(l)):
        if i % 3 != 0:
            a.append(l[i])
        else:
            b.append(l[i])
    b.sort()
    for i in range(len(l)):
        if i % 3 != 0:
            l[i] = a.pop(0)
        else:
            l[i] = b.pop(0)
    return l

