

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # 1. Create an empty list
    # 2. Go through the list
    # 3. If the item is not in the empty list
    # 4. Add it to the empty list
    # 5. Return the empty list

    new_l = []
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return new_l

