def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates
    return sum(x != y for x, y in zip(arr, reversed(arr))) // 2