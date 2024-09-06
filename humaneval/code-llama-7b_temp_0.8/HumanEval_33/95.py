

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0 or len(l) % 3 == 0:
        return l
    ret = l.copy()
    length = len(l)
    for i in range(0, length, 3):
        a = l[i]
        b = l[i + 1]
        c = l[i + 2]
        if a <= b and b <= c:
            continue
        if a <= c and c <= b:
            ret[i + 1] = a
            ret[i + 2] = b
            ret[i] = c
        else:
            ret[i + 1] = c
            ret[i + 2] = a
            ret[i] = b
    return ret


