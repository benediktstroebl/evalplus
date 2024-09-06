Here's a self-contained Python function that filters out integers from a given list:
```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_cases = {
    'test_values': test_values,
    'expected': [5],  # integers only!
}

for name, data in test_cases.values():
    actual = filter_integers(data)
    assert actual == test_cases[name]
```
This code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the original list. The test cases are defined to verify the function's correctness by passing different lists of values and comparing the output with the expected integers.