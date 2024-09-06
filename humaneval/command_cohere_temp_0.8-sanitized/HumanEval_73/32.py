def smallest_change(arr):
    changes = 0
    for a in arr:
        if a != arr[::-1].index(a):
            changes += 1
    return changes