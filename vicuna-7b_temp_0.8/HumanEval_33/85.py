

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    i, j = 0, 0
    while i < len(l) and j < len(l) // 3:
        if i + j > len(l) // 3:
            break
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1
    return l