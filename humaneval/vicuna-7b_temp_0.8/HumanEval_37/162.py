

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_odd = l[:]
    l_even = l
    while l_odd and l_even:
        if l_odd[0] > l_even[0]:
            l_odd = l_odd[1:]
            l_even = l_even[1:]
        else:
            l_odd = l_odd[1:] + [l_odd[0]]
            l_even = l_even[1:] + [l_even[0]]
    return l_odd + l_even
