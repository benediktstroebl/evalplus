

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_e = []
    for i in range(0, len(l), 2):
        if i + 1 < len(l):
            l_e.append(l[i + 1])
        else:
            break
    l_e.sort()
    l_e = l_e[::-1]
    for i in range(len(l) // 2, len(l), 2):
        l[i] = l_e[i - len(l) // 2]
    return l

