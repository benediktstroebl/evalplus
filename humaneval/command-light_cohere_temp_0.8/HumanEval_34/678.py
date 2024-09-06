```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-0, None]]

# Test cases
tests = [
    lambda: unique([5, 3, 5, 2, 3, 3, 9, 0, 123]),
    [0, 2, 3, 5, 9, 123]
]

for test_case, expected in tests:
    actual = unique(test_case)
    print(f"Test {test_case}: {actual} -> {expected}")
```