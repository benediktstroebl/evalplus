

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Indexes to store the even elements of the original list
    sorted_list = []
    # For every element in the original list...
    for index in range(1, len(l), 2):
        sorted_list.append(l[index])
    # For every even element in the original list...
    for element in range(0, len(l) - 1, 2):
        # Store the element in the even index position in the sorted list
        sorted_list.append(l[element])
    # Return the list of the sorted elements in even position
    return sorted_list
