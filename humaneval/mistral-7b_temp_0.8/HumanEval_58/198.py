

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    # loop through list 1
    # if a value is not in list 2 then don't add it
    # to list_found

    # if a value is in list 2, add it to list_found
    # if the value is already in list_found, do nothing

    # after loop through list 1
    # return list_found

    list_found = []

    for elem in l1:
        if elem in l2 and elem not in list_found:
            list_found.append(elem)

    return list_found
