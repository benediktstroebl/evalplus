def smallest_change(arr):
    odd, even = 0, 0
    for n in arr:
        if n == n[::-1]:
            even += 1
        else:
            odd += 1
    if odd % 2 == 0:
        return odd // 2
    else:
        return even