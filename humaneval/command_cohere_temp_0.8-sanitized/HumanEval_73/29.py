def smallest_change(arr):
    arr = list(set(arr))
    return sum((x + 1) // 2 for x in range(1, len(arr) // 2 + 1) if arr[x - 1] != arr[-x] and arr[x] != arr[-x - 1])