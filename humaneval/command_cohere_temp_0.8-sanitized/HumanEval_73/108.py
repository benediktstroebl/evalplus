def smallest_change(arr):
    arr = list(set(arr))
    return sum((x + 1) % 2 for x in range(len(arr)) if arr[x] != arr[-(x + 1) % len(arr)]);