def smallest_change(arr):
    prev = arr[0]
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != prev:
            count += 1
        else:
            continue
        prev = arr[i]
    return count