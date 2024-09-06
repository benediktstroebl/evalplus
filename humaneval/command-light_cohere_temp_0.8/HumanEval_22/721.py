```python
def filter_integers(values): 
    """Filter given list of any python values only for integers."""
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = ['a', 3.14, 5]
assert filter_integers(test_values) == [5]

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
assert filter_integers(test_values) == [1, 2, 3]

# Test case 3
test_values = [True, False, 3. performed with [int])
assert filter_integers(test_values) == [3]
```