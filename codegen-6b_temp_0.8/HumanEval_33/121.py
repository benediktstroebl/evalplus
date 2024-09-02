

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
    # l = l[:]
    # l.sort()
    return [l[i] for i in range(len(l)) if i % 3 == 0 and l[i] != l[i + 1]] + \
        [l[i] for i in range(len(l)) if i % 3 != 0 and l[i] != l[i + 1]]
    """
    l = l[:]
    l.sort()
    i = 0
    j = 1
    k = 2
    while i < len(l) and j < len(l) and k < len(l):
        if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
            l[i], l[j], l[k] = l[j], l[k], l[i]
            i += 1
            j += 1
            k += 1
        elif l[i] == l[j] and l[i] != l[k]:
            i += 2
            j += 2
        elif l[j] == l[k] and l[j] != l[i]:
            j += 2
            k += 2
        elif l[k] == l[i]:
            k += 2
            i += 2
        elif l[i] != l[j]:
            i += 2
            j += 2
    # l[:] = l[:i] + l[k:]
    return l[:k] + l[i:]

