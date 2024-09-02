

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    i = 0
    sorted_l = []
    while i < len(l):
        if i % 2 == 0:
            sorted_l.append(sorted(l[i:i+1]))
        else:
            sorted_l.append(l[i])
        i += 1
    return sorted_l

