def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            break
        if arr[i] > arr[ans]:
            ans = i
    return ans if ans != len(arr) - 1 else -1