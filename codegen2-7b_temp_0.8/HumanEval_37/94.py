

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_len = len(l)
    l_even = list(l[::2])
    l_odd = list(l[1::2])
    l_even = sorted(l_even)
    l_odd = sorted(l_odd)
    l_even = [l_even[i] for i in range(l_len)]
    l_even.extend(l_odd)
    return l_even
