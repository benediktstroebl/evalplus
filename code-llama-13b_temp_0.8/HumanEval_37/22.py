

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # First we make a copy of the list
    l_copy = l[:]
    # Now we iterate through each even index in l
    for i in range(0, len(l_copy), 2):
        # We swap the value at the current even index for the smallest value in the list after it
        min_index = min_index_after(l_copy, i)
        swap(l_copy, min_index, i)
    # Then we return the copy
    return l_copy
