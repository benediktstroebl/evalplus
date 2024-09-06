

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = list(l)
    l_len = len(l)
    l_even = []
    l_odd = []
    for i in range(l_len):
        if i % 2 == 0:
            l_even.append(l_copy[i])
        else:
            l_odd.append(l_copy[i])
    l_even.sort()
    new_l = []
    for i in range(l_len):
        if i % 2 == 0:
            new_l.append(l_even[i])
        else:
            new_l.append(l_odd[i])
    return new_l

