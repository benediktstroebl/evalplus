```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): A list of numbers.

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines the `monotonic` function that checks if the elements in the input list `l` are either monotonically increasing or decreasing. It uses the `all` function to ensure that this condition holds for all elements in the list except the last one. The function then returns `True` if the list is monotonically increasing or decreasing and `False` otherwise.