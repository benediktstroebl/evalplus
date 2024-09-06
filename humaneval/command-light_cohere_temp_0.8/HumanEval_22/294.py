```python
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> print(filter_integers(['a', 3.14, 5]))
    [5]
    >>> print(filter_integers([1, 2, 3, 'abc', {}, []]))
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]
```