```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test cases
test_get_positive = []
test_cases = [
    [],
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for case in test_cases:
    test_get_positive = get_positive(case)
    assert len(test_get_positive) == 6  # Negative test, should return empty list
    assert all(test_get_positive) == [2, 5, 6]  # Positive numbers should be there

# Output
[2, 5, 6]

# Success!
```