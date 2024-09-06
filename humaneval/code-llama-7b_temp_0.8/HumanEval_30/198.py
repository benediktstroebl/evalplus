

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # The list to store positive numbers in
    result = []

    # Loop through the list
    for item in l:
        # If the item is positive, append it to the list of positive numbers
        if item >= 0:
            result.append(item)

    return result

