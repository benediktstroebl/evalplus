```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_cases = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for test_case in test_cases:
    actual_positive = get_positive(test_case)
    expected = [2, 5, 6]  # Adjusted list as per your needs
    test_get_positive.assertEqual(actual_positive, expected)
```