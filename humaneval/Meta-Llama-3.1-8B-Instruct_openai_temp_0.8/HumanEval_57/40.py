```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements to check.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 4, 5]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # True
print(monotonic([1, 1, 1, 1, 1]))  # True
```

This script defines a function `monotonic` that checks if a list of elements is monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if all adjacent pairs of elements in the list satisfy the monotonicity condition. If the list is monotonically increasing, `l[i] <= l[i+1]` will be true for all `i`, and if the list is monotonically decreasing, `l[i] >= l[i+1]` will be true for all `i`.