

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l = sorted(l)
    if not l[::2] == l:
        i = 0
        for j in range(0, len(l), 2):
            if l[j] > l[j+1]:
                l[i], l[i+1] = l[i+1], l[i]
                i += 1
    return l