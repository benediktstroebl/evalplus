def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd % 2 == 0:
        return odd // 2
    else:
        return (odd + 1) // 2