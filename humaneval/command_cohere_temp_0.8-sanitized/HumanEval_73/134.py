def smallest_change(arr):
    odd, even = 0, 0
    for n in arr:
        if n == n[::-1]:
            even += 1
        else:
            odd += 1
    return min(odd, even)