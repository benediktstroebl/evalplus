def monotonic(lst):
    if len(lst) <= 1:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a <= b:
            # All elements are monotonically increasing
            if a == b:
                return True
            a = b
        else:
            return False
    return True