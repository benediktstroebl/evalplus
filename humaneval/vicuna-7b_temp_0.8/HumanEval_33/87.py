

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
    j = 0
    k = 0
    while i < len(l) - 1:
        if l[i] % 3 == 0 and l[i] != l[j]:
            l[k] = l[i]
            i += 1
            j += 1
            k += 1
        else:
            l[k] = l[i]
            i += 1
        k += 1
    return l
