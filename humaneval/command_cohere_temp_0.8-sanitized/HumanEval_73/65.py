def smallest_change(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            count += 1
    return count