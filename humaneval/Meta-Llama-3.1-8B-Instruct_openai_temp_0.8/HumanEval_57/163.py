```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. It uses the `all` function to check if the condition `l[i] <= l[i+1]` holds for all `i` (for increasing list) or `l[i] >= l[i+1]` holds for all `i` (for decreasing list). The function returns `True` if either of these conditions is met. The test cases at the end demonstrate the function's usage.