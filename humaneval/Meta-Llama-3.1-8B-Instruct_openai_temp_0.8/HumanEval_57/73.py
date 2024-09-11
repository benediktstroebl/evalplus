```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or \
           all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines the `monotonic` function, which takes a list of numbers as input. It uses the `all` function in combination with list comprehensions to check whether the list is monotonically increasing or decreasing. The `all` function returns `True` if all elements of the iterable (in this case, the list comprehensions) are true. 

If the list is of length 1 or less, the function returns `True` since a single element or no elements at all is trivially monotonically increasing or decreasing.

The test cases at the end show the function's behavior on different inputs.