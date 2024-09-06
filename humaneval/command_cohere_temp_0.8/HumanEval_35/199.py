```python
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    return max(l)
```

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list using the `max` function. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # 3
```

And here is the function’s documentation:
```
Returns:
    int: The maximum element in the list.

Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
```

As shown in the documentation, the function correctly returns the maximum element in the list, irrespective of any negative values or zeroes.