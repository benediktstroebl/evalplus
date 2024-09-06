```python
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> ['a', 3.14, 5] == [5]
    >>> [1, 2, 3, 'abc', {}, []] == filter_integers([1, 2, 3, 'abc', {}, []])
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```