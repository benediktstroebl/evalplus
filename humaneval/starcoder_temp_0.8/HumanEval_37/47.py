

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = l[::2]
    l2 = l[1::2]
    l2.sort()
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3
