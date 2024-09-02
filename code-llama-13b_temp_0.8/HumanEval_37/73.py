

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Empty list
    if len(l) == 0:
        return l
    # Base case
    if len(l) == 1:
        return l
    # Inductive step
    else:
        even = sort_even(l[1::2])
        odd = l[0::2]
        return [x for pair in zip(even, odd) for x in pair]
