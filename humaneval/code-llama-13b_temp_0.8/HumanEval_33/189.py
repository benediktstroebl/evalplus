

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    res = []
    i = 0
    while i < len(l):
        if i % 3 == 0:
            new_sub = []
            for j in range(3):
                new_sub.append(l[i + j])
            new_sub.sort()
            for k in range(3):
                res.append(new_sub[k])
            i += 3
        else:
            res.append(l[i])
            i += 1
    return res


