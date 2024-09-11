```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    A list is considered monotonically increasing if all elements are in
    ascending order, and monotonically decreasing if all elements are in
    descending order.

    Args:
        lst (list): A list of elements.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))   # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. It uses two helper lists, one to check for increasing order and another for decreasing order, and returns `True` if either condition is met. The test cases at the end demonstrate the function's usage.