

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Assign l' an empty list
    l' = []
    # For each index in l
    for index in range(len(l)):
        # If the index is odd
        if index % 2 == 1:
            # Append l[index] to l'
            l'.append(l[index])
        # Otherwise
        else:
            # Append l[index] to l'
            l'.append(sorted(l[index])[0])
    # Return l'
    return l'

