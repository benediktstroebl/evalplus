def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a <= b:
            # Increasing, this is the happy case
            if a == b:
                return False  # Equal elements not allowed
            a = b
        else:
            # Decreasing, make sure the increments are small enough
            if a - b >= lst[1] - lst[0]:
                return False
            a = b
    return True