

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
    j = len(l) - 1
    while i < j:
        while i < j and l[i] % 3 == 0:
            i += 1
        while i < j and l[j] % 3 == 0:
            j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
        i += 1
    return l
