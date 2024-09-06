def monotonic(lst):
    """Returns True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi = lst[0], lst[-1]
    for x in lst[1:-1]:
        if x <= lo or x >= hi:
            return False
        lo, hi = x, x
    return True