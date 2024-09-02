

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    assert(len(l) > 2), 'This function takes maximum a list of length 3'
    i = 0
    while i < len(l):
        if i % 3 == 0:
            l[i] = l[i]
        else:
            j = i - 1
            while j >= 0 and l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                j -= 1
        i += 1
    return l