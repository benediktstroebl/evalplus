

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Make a new list to be filled by unique elements.
    new_list = []

    # Traverse through the list and add elements to
    # the new_list if they are not present in new_list
    for x in l:
        if x not in new_list:
            new_list.append(x)

    # Sort the new_list and return it
    new_list.sort()
    return new_list
