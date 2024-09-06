

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = l[1::2]
    l2.sort()
    i = 0
    for item in l:
        if i % 2 == 0:
            l2.append(item)
        i += 1
    l2.extend(l[::2])
    return l2

