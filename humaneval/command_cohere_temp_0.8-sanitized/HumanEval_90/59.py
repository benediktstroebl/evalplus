def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    ls = sorted(lst)
    return ls[1] if len(ls) >= 2 else None