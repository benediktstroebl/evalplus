def smallest_change(arr):
    arr.sort()
    diff = abs(arr[-1] - arr[0])
    return diff if diff <= len(arr) // 2 else len(arr)