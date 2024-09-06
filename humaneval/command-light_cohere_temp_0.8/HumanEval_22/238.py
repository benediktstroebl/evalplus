```python
def filter_integers(values):
    """Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Tests
print(filter_integers(['a', 3.14, 5]))      # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 97, 3, 999, 123, 'abc', 42])) # [10, 97, 3, 123]
```