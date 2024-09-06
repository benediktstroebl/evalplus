def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    try:
        diff = l[1:] - l[:-1]
        return diff.min() >= 0
    except Exception:
        return False