def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates to handle cases like [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    return sum(x != y for x, y in zip(arr, reversed(arr))) // 2     # Count changes and divide by 2