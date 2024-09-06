def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1] and arr[i] != prev:
            prev = arr[i]
            ans = i
        elif arr[i] < arr[i - 1] and arr[i] == prev:
            break
    else:
        ans = -1
    return ans