def smallest_change(arr):
    odd, even = 0, 0
    for i in range(len(arr)):
        if arr[i] % 2:
            odd += 1
        else:
            even += 1
    return min(odd, even)