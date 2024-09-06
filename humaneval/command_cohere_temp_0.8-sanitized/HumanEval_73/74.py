def smallest_change(arr):
    prev = arr[0]
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
        if arr[i] != prev:
            prev = arr[i]
    return count