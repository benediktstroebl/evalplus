def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]