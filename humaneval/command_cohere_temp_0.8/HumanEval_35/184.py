```python
def max_element(l: list):
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
The function `max_element` takes a list `l` as an argument and returns the maximum element in the list using the `max` function. The behavior of the `max` function is explicitly tested for uniqueness in the function specification. Thus, there is no need to add additional tests for this function.