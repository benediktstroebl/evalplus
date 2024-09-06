```python
def max_element(l: list):
    """Return maximum element in the list
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    >>> l = [1, 2, 3, -5, -10]
    >>> max_element(l) 
    -10
    >>> l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> max_element(l) 
    10
    """
    return max(l)
```