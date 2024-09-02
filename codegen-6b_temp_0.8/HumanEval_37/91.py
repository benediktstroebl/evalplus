

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_even = l[1::2]
    l_odd = l[0::2]
    l_even.sort()
    l_list = [l_odd[i] for i in range(len(l_odd))]
    l_list.extend(l_even)
    return l_list