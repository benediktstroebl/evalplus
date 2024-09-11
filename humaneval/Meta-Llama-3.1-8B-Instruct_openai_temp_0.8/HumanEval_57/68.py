```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of elements.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if list is empty or only contains one element
    if len(l) <= 1:
        return True  # An empty list or a list with one element is monotonically increasing/decreasing

    # Check if list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))

    # Check if list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))

    # Return True if list is either monotonically increasing or decreasing
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # Output: True
print(monotonic([1, 20, 4, 10]))  # Output: False
print(monotonic([4, 1, 0, -10]))  # Output: True
```

This script defines a function `monotonic(l)` that checks if the elements in the list `l` are monotonically increasing or decreasing. It returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check for monotonicity in both the increasing and decreasing directions. It also handles edge cases such as empty lists and lists with a single element.