```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of integers.

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic(l)` that checks if the input list `l` is monotonically increasing or decreasing. It uses the `all()` function with a generator expression to check if all adjacent elements in the list satisfy the condition of being either less than or equal to, or greater than or equal to. The `or` keyword is used to allow for both increasing and decreasing monotonicty. The test cases at the end demonstrate the function's behavior.