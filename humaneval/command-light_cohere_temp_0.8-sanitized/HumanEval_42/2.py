def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l