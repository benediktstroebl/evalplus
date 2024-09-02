

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # We need to sort the list to get an ordered list of elements.
    # The list we return must be ordered too so it is sorted.
    l1 = sorted(l1)
    l2 = sorted(l2)

    result = []
    i = 0
    while i < len(l1) and i < len(l2):
        if l1[i] == l2[i]:
            # If elements are the same, add them to the result
            # and increment the indexes.
            result.append(l1[i])
            i += 1
        else:
            # If elements are different, increment the index of the
            # smaller one, because we know that we won't find it
            # in the other list.
            if l1[i] < l2[i]:
                i += 1
            else:
                i += 1

    return result

