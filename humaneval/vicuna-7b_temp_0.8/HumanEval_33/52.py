

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
    i = j = n // 3
    while i < n:
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1
        elif l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
            i += 1
        else:
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                i += 2
            j += 1
    return l
