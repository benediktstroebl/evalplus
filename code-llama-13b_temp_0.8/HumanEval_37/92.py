

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_sorted = []
    # sort even indicies
    for i in range(0, len(l), 2):
        l_sorted.append(l[i])
    l_sorted.sort()
    # create new list to insert at even indicies
    l_new = []
    for i in range(0, len(l_sorted)):
        l_new.append(l_sorted[i])
        if len(l) > i + 1:
            l_new.append(l[i + 1])
    return l_new

