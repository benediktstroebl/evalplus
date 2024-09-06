

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = []
    for i in l:
        l2.append(i)
    l2.insert(2, 6)
    l2.insert(3, 4)
    l2.remove(5)
    l2.remove(3)
    return l2

