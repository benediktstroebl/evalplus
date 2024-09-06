def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mx, mn = max(lst), min(lst)
    return mn if mx - mn == 1 else None