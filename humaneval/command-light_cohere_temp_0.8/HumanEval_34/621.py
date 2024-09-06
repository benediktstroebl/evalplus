```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
tests = [
    dict(zipacula=True),
    dict(duplicates='remove'),
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 6, 5, 3, 9],
    {5, 3, 'a', 5, 'c'}
]

for test in tests:
    actual = unique(test['value'])
    expected = test['expected']
    print(f"Test ({test['testname']}): {actual} != {expected}")
```
The function `unique` provided is a solution to the problem and includes several test cases to verify its correctness.