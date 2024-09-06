def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    return all(l[i] <= l[i+1] or l[i] >= l[i+1] for i in range(len(l)-1))