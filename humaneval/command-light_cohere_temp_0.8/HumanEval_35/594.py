```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    >>> l = [4, 3, 2, 2, -20, -47]
    >>> max_element(l)
    -20
    """
    return max(l)
```
This code defines a Python function `max_element` that takes an argument `l`, which is expected to be a list. The function returns the max element of the list passed as an argument, using the `max()` function from the built-in `numpy` library. The use of `max()` allows us to get the maximum value from a given input.