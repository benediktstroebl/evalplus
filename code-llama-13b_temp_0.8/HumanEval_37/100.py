

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # copy the list l and call the copy l'
    l_dash = l.copy()
    # list to store the even indicies of l_dash
    even_indices = []
    # loop through l_dash to find the even indicies
    for i in range(len(l_dash)):
        if i % 2 == 0:
            even_indices.append(i)
    # list to store the even indicies of l_dash
    even_values = []
    # loop through the even indicies of l_dash
    for i in even_indices:
        # append the value at the even indicies to the list even_values
        even_values.append(l_dash[i])
    # sort the list of values at the even indicies
    even_values.sort()
    # loop through the list of values at the even indicies
    for i in range(len(even_values)):
        # at the i_th even index, replace the value with the i_th value in even_values
        l_dash[even_indices[i]] = even_values[i]
    # return the sorted list l'
    return l_dash
