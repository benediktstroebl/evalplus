

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    i = 0
    j = 1
    k = 2
    l_set = set(l)
    while i < len(l) - 1:
        while j < len(l) - 1:
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            i += 1
            j += 1
        if k < len(l) - 1:
            while k < len(l) - 1:
                if l[k] > l[k + 1]:
                    l[k], l[k + 1] = l[k + 1], l[k]
                k += 1
        i = 0
        j = 1
        k = 2
    return l


