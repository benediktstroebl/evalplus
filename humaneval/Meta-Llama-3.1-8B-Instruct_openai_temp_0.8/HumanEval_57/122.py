```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list of elements.

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
    return all(
        l[i] <= l[i + 1] for i in range(len(l) - 1)
    ) or all(
        l[i] >= l[i + 1] for i in range(len(l) - 1)
    )

# Test cases
print(monotonic([1, 2, 4, 20]))   # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 2, 3]))    # True
print(monotonic([3, 2, 2, 1]))    # True
print(monotonic([1, 2, 2, 5]))    # False
```

This script uses the `all()` function to check if all elements in the list meet the condition. If the list is monotonically increasing, all elements `l[i]` should be less than or equal to the next element `l[i + 1]`. If the list is monotonically decreasing, all elements `l[i]` should be greater than or equal to the next element `l[i + 1]`. The `or` operator is used to check both conditions.