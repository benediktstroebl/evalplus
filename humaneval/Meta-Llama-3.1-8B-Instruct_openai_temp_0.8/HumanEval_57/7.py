```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): List of elements.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
In this script, we define a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. We use the `all` function with a generator expression to check if all elements are either increasing or decreasing. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise. If the list is monotonically increasing or decreasing, the `all` function will return `True`, and if it's not, it will return `False`.