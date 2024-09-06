def smallest_change(arr):
    arr.sort()
    ind = len(arr) // 2
    if arr[ind] == arr[0]:
        return abs(ind - 1)
    return min(2 * ind + 1, min(arr[:ind].count(arr[ind]) + 1, arr[ind + 1:].count(arr[ind]) + 1))