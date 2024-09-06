```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123])
    123
    >>> max_element([3, 2, -10, -100])
    -100
    >>> max_element([])
    0
    >>> max_element([1, 2, 3, 4, 5])
    5
    """
    return max(l)
```