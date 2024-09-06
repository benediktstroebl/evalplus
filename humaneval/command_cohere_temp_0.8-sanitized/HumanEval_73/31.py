def smallest_change(arr):
    arr.sort()
    changes = abs(len(arr) - 2)
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            changes = changes + 1
    return changes