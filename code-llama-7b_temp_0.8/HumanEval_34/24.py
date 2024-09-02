

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Unique list
    u = []

    # Traverse through the sequence
    for seq in l:

        # Check if exists in u or not
        if seq not in u:
            u.append(seq)

    # Sort the unique list
    u.sort()

    # Return the list
    return u

