

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even = [l[i] for i in range(0, len(l), 2)]
    sorted_even = sorted(even)

    even_indices = [i for i in range(0, len(l), 2)]
    sorted_even_indices = sorted(even_indices)

    for i in range(len(sorted_even)):
        l[sorted_even_indices[i]] = sorted_even[i]

    return l

