def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for num in lst:
        if num > mn and num < mx and num != sm:
            sm = num
    return sm if sm != mn else None