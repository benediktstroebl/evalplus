```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    [],
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

# Function tests
assert(filter_integers(test_filter_integers)), "Error: Function returned non-integer values")
```