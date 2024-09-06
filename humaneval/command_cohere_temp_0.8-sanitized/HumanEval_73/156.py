def smallest_change(arr):
    odd, even = 0, 0
    for num in arr:
        if num == num[1:] + num[:1]:
            even += 1
        else:
            odd += 1
    return min(odd, even)