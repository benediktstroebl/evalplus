def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd%2 == 1:
        return len(arr) // 2
    else:
        return len(arr) // 2 - 1