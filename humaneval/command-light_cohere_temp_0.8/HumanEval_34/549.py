```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test cases
tests = [
    [listographies = [5, 3, 5, 2, 3, 3, 9, 0, 123], ['a', 'b', 'c', 'd'], ],
    [[]],
]

for test_case in tests:
    actual = unique(test_case)
    expected = [x for x in test_case if x not float]
    assert actual == expected, "Expected: {} but got: {}".format(expected, actual)
```