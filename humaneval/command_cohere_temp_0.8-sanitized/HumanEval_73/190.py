def smallest_change(arr):
    changed = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changed += 1
    return changed