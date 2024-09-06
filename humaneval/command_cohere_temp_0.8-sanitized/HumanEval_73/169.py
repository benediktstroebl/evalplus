def smallest_change(arr):
    even, odd = 0, 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)