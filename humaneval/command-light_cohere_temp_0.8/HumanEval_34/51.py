```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'bb', 'ccc'],
    ['text', 'bottom', 'some']
]

for test in tests:
    assert unique(test) == [0, 2, 3, 5, 9, 123, 4, 6, 7, 'a', 'bb', 'ccc']
```

This script defines a function `unique` that sorts and returns unique elements from an input list. The test cases are provided to ensure the function's correctness.