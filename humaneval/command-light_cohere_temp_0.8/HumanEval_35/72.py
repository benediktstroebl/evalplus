```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not isinstance(l, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(x, (int, float)) for x in l):
        raise ValueError("All elements in the list should be numbers")
    max_element = max(l)
    return max_element
```