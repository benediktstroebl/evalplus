

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    """
    if len(l) == 0:
        return l
    else:
        i = 0
        while i < len(l) and not (i % 3 == 0):
            i += 1
        if i < len(l):
            return [l[i]] + sort_third(l[:i]) + sort_third(l[i+1:])
        else:
            return []
    """
    for i in range(0, len(l), 3):
        if i < len(l) - 2:
            l[i+1:i+3] = sorted(l[i+1:i+3])
        else:
            l[i:i+3] = sorted(l[i:i+3])
    return l
