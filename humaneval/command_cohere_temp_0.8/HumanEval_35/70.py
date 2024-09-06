```python
def max_element(l: list):
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        raise ValueError("Input list is empty")
    
    max_element = max(l)
    return max_element
```

The function `max_element` takes a list `l` as input and returns the maximum element in the list. It first checks if the list is empty, raising a `ValueError` if so. It then finds the maximum element using the `max` function and returns it.

This code passes the given tests because:
- It handles the case of an empty list correctly.
- It efficiently finds the maximum element using the built-in `max` function.