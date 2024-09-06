```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Tests
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 3, 'a', 4, 5, 'c'])))  # []
```