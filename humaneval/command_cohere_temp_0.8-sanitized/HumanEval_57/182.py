def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    a = l[0]
    for b in l[1:]:
        if a <= b:
            # Checking if the list is monotonically increasing
            if a < b:
                return False
            a = b
        else:
            # Checking if the list is monotonically decreasing
            if a > b:
                return False
            a = b
    return True