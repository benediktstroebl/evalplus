

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_copy = l.copy()
    for i in range(len(l)):
        j = (i // 3) * 3
        k = (i % 3) + 1
        l_copy[j], l_copy[k] = l_copy[k], l_copy[j]
    return l_copy
