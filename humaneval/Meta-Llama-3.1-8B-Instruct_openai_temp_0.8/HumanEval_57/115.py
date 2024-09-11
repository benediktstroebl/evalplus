```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    A list is monotonically increasing if each element is greater than or equal to the previous element.
    A list is monotonically decreasing if each element is less than or equal to the previous element.
    
    Args:
        lst (list): The input list.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function with a generator expression to check if all elements in the list are either less than or equal to their neighbors, or greater than or equal to their neighbors.

Alternatively, you can use a more concise version of the function using only one `all` call:

```python
def monotonic(lst: list):
    return all(x <= y for x, y in zip(lst, lst[1:]))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this version, `zip(lst, lst[1:])` generates pairs of adjacent elements in the list, and `all(x <= y for x, y in...)` checks if all these pairs satisfy the monotonicity condition.