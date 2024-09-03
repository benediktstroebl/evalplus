def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) == 0:
        return False
    # For each element, check if it is less or greater than the previous
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return True
    return False