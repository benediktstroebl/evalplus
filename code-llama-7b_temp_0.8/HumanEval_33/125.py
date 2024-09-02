

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) == 0:
        return l
    else:
        m = 1
        while m < len(l):
            if m % 3 == 0:
                m += 1
            else:
                break
        i = m
        while i < len(l):
            if i % 3 != 0:
                l[i], l[i - m] = l[i - m], l[i]
            i += 1
        return l

