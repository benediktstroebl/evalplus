```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_cases = [test_values[i:]filter_integers(test_values) for i in range(len(test_values))]

# Verify results
assert all([x == [i] for x, i in zip(test_values, test_cases))]
```