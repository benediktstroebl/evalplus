```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    A list is monotonically increasing if each element is greater than or equal to the previous one.
    A list is monotonically decreasing if each element is less than or equal to the previous one.

    Args:
    l (list): The input list to check.

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
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the elements are either monotonically increasing or decreasing, and `False` otherwise. It uses a generator expression to check this condition for both increasing and decreasing lists, and the `all` function to make sure that the condition is met for all pairs of adjacent elements in the list. The script also includes test cases to verify the correctness of the function.