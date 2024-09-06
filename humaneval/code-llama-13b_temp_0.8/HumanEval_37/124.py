

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Even indicies of the list are in even_vals
    even_vals = l[::2]
    # Odd indicies of the list are in odd_vals
    odd_vals = l[1::2]
    # Sort even_vals
    even_vals.sort()
    # Build the sorted list
    sorted_l = []
    # For the first half of the list
    for index in range(0, len(l) // 2):
        # Add an even value
        sorted_l.append(even_vals[index])
        # Add an odd value
        sorted_l.append(odd_vals[index])
    # Return the sorted list
    return sorted_l


