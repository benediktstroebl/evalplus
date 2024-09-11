```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the elements in the list are monotonically increasing or decreasing, and `False` otherwise. The function uses a generator expression with the `all` function to check if all consecutive pairs of elements in the list satisfy the condition of being either monotonically increasing or decreasing. The test cases at the end of the script demonstrate the function's behavior with different input lists.