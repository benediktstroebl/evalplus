

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = l[:]
    l1.reverse()
    l.extend(l1)
    # import pdb; pdb.set_trace()
    l2 = [l[i] for i in range(0, len(l), 2)]
    l3 = [l[i] for i in range(1, len(l), 2)]
    l4 = sorted(l2)
    l5 = sorted(l3)
    l6 = l4 + l5
    return l6

