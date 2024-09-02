

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    n = len(l)
    i = j = 0
    while j < n // 3:
        i += 1
        while l[i] == l[j]:
            j += 1
        l[i], l[j] = l[j], l[i]
        j += 1
    return l