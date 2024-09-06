def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    try:
        diff = l[1:] - l[:-1]
        return all(x >= 0 or x < 0 for x in diff)
    except IndexError:
        return False