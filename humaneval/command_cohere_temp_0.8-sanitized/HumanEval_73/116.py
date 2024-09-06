def smallest_change(arr):
    changed = 0
    for a in arr:
        if a != arr[::-1].index(a):
            changed += 1
    return changed