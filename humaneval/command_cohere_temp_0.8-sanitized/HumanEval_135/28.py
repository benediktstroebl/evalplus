def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        if arr[i] > prev:
            ans = i
        prev = arr[i]
    return -1 if ans == 0 else ans