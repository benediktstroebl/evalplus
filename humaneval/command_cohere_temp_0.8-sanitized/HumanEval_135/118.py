def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= prev:
            continue
        arranged = i
        break
    return arranged