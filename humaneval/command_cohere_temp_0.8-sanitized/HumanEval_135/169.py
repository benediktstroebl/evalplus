def can_arrange(arr):
    prev = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            idx = i + 1
            break
    return idx if idx > 0 else -1