

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Define a list l' containing the same elements as l, but sorted
    # In case l is empty, return l
    if not l:
        return l
    else:
        # Sort the list in ascending order
        l_sorted = sorted(l)
        # Create a new list l' containing the first half of the sorted list
        # and the remaining list sorted in descending order
        l_half_asc = l_sorted[:len(l_sorted)//2]
        l_half_desc = l_sorted[len(l_sorted)//2:]
        return l_half_asc + l_half_desc
