def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            count += 1
    return count