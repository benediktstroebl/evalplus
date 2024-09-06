def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    try:
        iter_ = iter(l)
        x = next(iter_)
        prev = x
        for y in iter_:
            if x <= prev <= y or x >= prev >= y:
                return True
            prev = y
    except:
        return False
    return False