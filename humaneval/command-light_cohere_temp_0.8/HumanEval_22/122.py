```python
def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [0]]
values2 = [5, 6, 7.ills, '8', 10, 20]

assert filter_integers(values1) == [1, 2, 3]
assert filter_integers(values2) == [5, 6, 7, 8, 10, 20]
```