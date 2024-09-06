

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l = l[:]
    odd_i = 0
    for i, elem in enumerate(l):
        if i % 2 == 1:
            l[odd_i] = elem
            odd_i += 1
    return l[:odd_i] + sorted(l[odd_i:])
