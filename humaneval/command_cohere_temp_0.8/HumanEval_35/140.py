```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
The function `max_element` takes a list `l` as an argument and returns the maximum element in the list. This is achieved using the `max` Python function, which returns the maximum value in a list. The behavior of the function is demonstrated by the provided test cases in the docstring, which also show how to call the function correctly.  It is a direct and efficient solution to find the maximum element in a list.