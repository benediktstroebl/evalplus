def smallest_change(arr):
    arr = list(set(arr))
    return sum((arr[i] != arr[-1-i] for i in range(len(arr) // 2)))