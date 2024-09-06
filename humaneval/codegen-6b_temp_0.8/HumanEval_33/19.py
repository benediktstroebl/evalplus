

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # duplicate l and sort.
    # after duplicate, remove every 3d element from the duplicate
    # return the rest of duplicate
    l_dup = l * 2
    l_dup = sorted(l_dup)
    l_dup = l_dup[len(l_dup) / 3:]
    ln = []
    for i in l_dup:
        if i not in ln:
            ln.append(i)

    return ln

