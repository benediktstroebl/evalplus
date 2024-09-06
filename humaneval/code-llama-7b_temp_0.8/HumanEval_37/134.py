

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_odd = l[1::2]
    l_even = l[0::2]
    sorted_l_even = sorted(l_even)
    l_return = []
    for i in range(len(sorted_l_even)):
        l_return.append(sorted_l_even[i])
        l_return.append(l_odd[i])

    return l_return

