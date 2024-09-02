

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Sort list
    sorted_list = sorted(l)
    # Make a new list
    new_list = []
    # Loop through list
    for i in range(len(sorted_list) - 1):
        # If the current element isn't the same as the previous element
        if sorted_list[i] != sorted_list[i + 1]:
            # Append the current element to the new list
            new_list.append(sorted_list[i])
    # Append the last element to the new list
    new_list.append(sorted_list[-1])
    # Return new list
    return new_list
