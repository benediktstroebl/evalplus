def monotonic(lst):
    """Returns True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi = lst[0], lst[-1]
    for num in lst[1:-1]:
        if num <= lo or num >= hi:
            return False
        lo, hi = num, num
    return True