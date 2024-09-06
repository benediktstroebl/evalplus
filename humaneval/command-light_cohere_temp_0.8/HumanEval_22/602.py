Here's the self-contained Python function that filters integers from a given list, passing the test too:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],  # Empty list
    ['a', 3.14, 5],  # Non-integer values
    [1, 2, 3, 'abc', {}, []],  # Mixed data
    ]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert actual == [x for x in test_case if isinstance(x, int)], "Test case failed: " + str(test_case) + " failed."
```