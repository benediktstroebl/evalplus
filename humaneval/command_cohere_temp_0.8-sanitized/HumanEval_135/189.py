def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            arranged = i - 1
            break
        prev = arr[i]
    return arranged