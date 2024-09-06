def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= prev:
            return arranged
        arranged = i
        prev = arr[i]
    return arranged