```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l), key=lambda x: x)

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 'abc'],
    ['a', 'b', 'c'],
    [set([1, 2])]
]

for case in test_cases:
    assert unique(case) == case
```