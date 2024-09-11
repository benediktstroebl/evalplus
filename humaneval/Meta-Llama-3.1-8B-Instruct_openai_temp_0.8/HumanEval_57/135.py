```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is monotonically increasing
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    
    # Check if the list is monotonically decreasing
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if a given list `l` is monotonically increasing or decreasing. It uses the `all` function with generator expressions to check if all adjacent pairs of elements in the list satisfy the condition for either an increasing or decreasing sequence. If the list satisfies either condition, the function returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior on different lists.