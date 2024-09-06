

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # ensure that the list is sorted
    l_sort = sorted(l)
    # now we remove duplicates starting from the left
    l_u = [l_sort[0]]
    l_u_set = set([l_sort[0]])
    for i in range(1, len(l_sort)):
        if l_sort[i] != l_sort[i-1]:
            l_u.append(l_sort[i])
            l_u_set.add(l_sort[i])
    return l_u
