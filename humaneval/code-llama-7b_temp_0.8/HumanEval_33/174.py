

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0:
        return l
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]
    l_new = []
    for i in range(3):
        l_new.append(l[i])
    m = l[2]
    l_new.sort()
    l_new.append(m)
    l = l_new
    return sort_third(l[1:])

