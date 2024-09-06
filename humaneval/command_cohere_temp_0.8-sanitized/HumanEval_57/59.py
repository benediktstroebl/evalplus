def monotonic(lst):
    if len(lst) <= 1:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a <= b:
            # Increasing: [a, a+1, a+2, ...]
            return True
        elif a >= b:
            # Decreasing: [a, a-1, a-2, ...]
            return True
        a = b
    return False