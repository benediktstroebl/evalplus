

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_copy = list(l)
    l_copy_even = l_copy[::2]
    l_copy_odd = l_copy[1::2]
    l_copy_even.sort()
    l_copy_odd.sort()
    l_copy.clear()
    for i in l_copy_even:
        l_copy.append(i)
    for i in l_copy_odd:
        l_copy.append(i)
    return l_copy

