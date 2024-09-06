def smallest_change(arr):
    odd, even = 0, 0
    for num in arr:
        if num % 2:
            odd += 1
        else:
            even += 1
    return min(odd, even)