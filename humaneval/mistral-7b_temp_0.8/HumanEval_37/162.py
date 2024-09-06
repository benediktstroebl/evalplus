

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """
    >>> l = [5, 6, 3, 4]
    >>> l[0], l[1], l[2], l[3]
    (5, 6, 3, 4)
    >>> l.sort()
    >>> l
    [3, 4, 5, 6]
    >>> l
    [3, 4, 5, 6]
    >>> l[0], l[1], l[2], l[3]
    (3, 4, 5, 6)
    >>> l
    [3, 4, 5, 6]
    >>> l
    [3, 4, 5, 6]
    >>> l.sort(reverse=True)
    >>> l[0], l[1], l[2], l[3]
    (6, 5, 4, 3)
    >>> l
    [6, 5, 4, 3]
    >>> l
    [6, 5, 4, 3]
    >>> l.sort(reverse=True)
