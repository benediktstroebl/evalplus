

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Iterate through l, adding [list(l)] if even, and [] if not
    new_list = [new_list if i % 2 == 0 else [] for i, new_list in enumerate(l)]
    # Sort the new list by the values of the even indices
    new_list.sort(key=lambda x: x[1])
    # Return the new list
    return list(chain.from_iterable(new_list))

