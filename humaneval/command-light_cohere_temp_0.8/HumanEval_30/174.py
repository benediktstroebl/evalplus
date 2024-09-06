```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various input
test_get_positive = get_positive
test_get_positive([-1, 2, -4, 5, 6])  # Expected output: [2, 5, 6]
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Expected output: [5, 3, 2, 3, 9, 123]
test_get_positive([1, 2, 3, -6, -4, -5])  # Expected output: []
test_get_positive([10, 2, 3, 4, 5])  # Expected output: [10, 2, 3, 4]
```