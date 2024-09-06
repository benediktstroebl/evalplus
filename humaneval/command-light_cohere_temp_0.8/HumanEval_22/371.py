```python
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function
values = [1, 2, 3, 'abc', {}, [1, 2, 3]]
assert filter_integers(values) == [1, 2, 3]
assert len(filter_integers([1, 2, 3, 'abc'])) == 3
assert len(filter_integers(['abc', 'abc'])) == 1
```