

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = l[0::2]
    l1.sort()
    l2 = l[1::2]
    l2.sort()
    l = []
    for x in range(len(l1)):
        l.append(l1[x])
        l.append(l2[x])


sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
