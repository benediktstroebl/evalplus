```python
def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([1, 2, 3, 'a', (5, 6))]
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Example usage
values_list = [1, 2, 3, 'abc', (5, 6)]
print(filter_integers(values_list))  # [1, 2, 3]
```