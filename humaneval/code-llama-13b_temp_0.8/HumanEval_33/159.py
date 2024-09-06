

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l.sort()

    for i in range(2, len(l), 3):
        if l[i] < l[i-1]:
            l[i-1], l[i] = l[i], l[i-1]
        if i + 1 < len(l) and l[i+1] < l[i]:
            l[i], l[i+1] = l[i+1], l[i]
        if i + 2 < len(l) and l[i+2] < l[i]:
            l[i], l[i+2] = l[i+2], l[i]
    return l
