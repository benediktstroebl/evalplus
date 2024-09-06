

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    copy = l.copy()
    i = 0
    while i < len(copy):
        if i % 3 == 0:
            list1 = copy[i::3]
            list2 = sorted(copy[i::3])
            for k in range(len(list1)):
                copy[i + k] = list2[k]
        i += 1
    return copy

