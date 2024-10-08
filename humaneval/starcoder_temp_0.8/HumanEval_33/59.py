

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
    while i < len(l):
        if l[i] % 3 == 0:
            j = i
        i += 1
    l_new = sorted(l[:j] + l[j+1:])
    l_new = l_new + l[j:j+1]
    return l_new
