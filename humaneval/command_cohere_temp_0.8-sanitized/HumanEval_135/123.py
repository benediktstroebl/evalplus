def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            ans = i + 1
            break
    return max(ans, -1)