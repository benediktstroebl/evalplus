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

    max_el = max(l)
    return max_el
```

The function `max_element` takes a list `l` as input and returns the maximum element in the list. It first checks if the list is empty, and if so, raises a `ValueError` with an appropriate message. Otherwise, it safely computes and returns the maximum element using the `max` function.

This code block solves the problem and provides documentation for the function, including example test cases in the docstring. It can be copied and pasted directly into a Python environment to use and further test as needed.