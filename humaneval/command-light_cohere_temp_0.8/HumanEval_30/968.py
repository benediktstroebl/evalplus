```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_cases = [
    [],
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Function execution and results
for test_case in test_cases:
    test_get_positive(test_case)
    assert all([num >= 0 for num in test_case]) == [True]
```