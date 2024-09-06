def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[::-1]):
        if a != b:
            changes += 1
    return changes