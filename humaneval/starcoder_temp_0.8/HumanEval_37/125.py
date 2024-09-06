

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = []
    l2 = []
    if len(l) % 2 == 0:
        for i in range(0, len(l), 2):
            l1.append(l[i])
            l2.append(l[i+1])
        return l1 + sorted(l2)
    else:
        for i in range(0, len(l)-1, 2):
            l1.append(l[i])
            l2.append(l[i+1])
        l1.append(l[-1])
        return l1 + sorted(l2)
