```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123])
    123
    >>> max_element([])
    0
    >>> max_element([9, 2, 0])
    9
    >>> max_element([123, 2, 2, 0])
    2
    >>> max_element([1, 2, 3, -1000])
    Traceback (most recent call last):
      ...
    ValueError: list index -1 out of bounds
```