```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test cases
tests = [
    [list=[5, 3, 5, 2, 3, 3, 9, 0, 123],],
    [set(),],
    [list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])],
]

for case in tests:
    actual = unique(case[0])
    expected = case[1]
    assert actual == expected, "Test case {} failed".
```