

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    #make a copy of the list
    l2 = list(l)
    #make a copy of even indicies
    l_even = l2[::2]
    #sort the copy
    l_even.sort()
    #set even indicies of l2 to those of l_even
    l2[::2] = l_even
    return l2
