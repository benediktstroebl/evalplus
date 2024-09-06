

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # l2 is l with the even indicies of l reversed
    l2 = list(reversed(l))
    l = []
    # pair the even indicies of l with their index in l2
    for i, item in enumerate(l2):
        if i % 2 == 0:
            l.append(item)
    # add the odd indicies of l
    for i in range(len(l2)):
        if i % 2 != 0:
            l.append(l2[i])
    return l


