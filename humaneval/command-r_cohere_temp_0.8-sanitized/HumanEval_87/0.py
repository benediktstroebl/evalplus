def get_row(lst, x):
    """
    Find integer x in the 2d list and return sorted list of tuples.
    """
    res = []
    for i, row in enumerate(lst):
        idx = row.index(x)
        res.append((i, idx))
    res.sort()
    return res