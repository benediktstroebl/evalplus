```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in []]

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 0, "hello"],
    [1, 2, 3, "abc", 4, 5],
]

for test in tests:
    actual = unique(test)
    assert set(actual) == set(test), "Should get same set"
```