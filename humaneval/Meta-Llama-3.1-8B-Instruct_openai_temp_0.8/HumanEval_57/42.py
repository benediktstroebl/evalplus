```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of elements.

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is empty
    if len(l) == 0:
        return True

    # Check if the list is monotonically increasing
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))

    # Check if the list is monotonically decreasing
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))

    # Return True if the list is either monotonically increasing or decreasing
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
print(monotonic([]))  # Expected: True
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing. It uses the `all` function with a generator expression to check if all adjacent elements in the list satisfy the condition of being monotonically increasing or decreasing. The function returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The script also includes test cases to verify the correctness of the function.