

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    assert len(l) % 3 == 0, "l must be a multiple of three"
    size = len(l) // 3
    l1 = l[:size]
    l2 = l[size:2 * size]
    l3 = l[2 * size:]
    l1.sort()
    l2.sort()
    l3.sort()
    return l1 + l2 + l3

"""
import doctest
doctest.testmod()
"""
