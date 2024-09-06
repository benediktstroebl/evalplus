```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with different inputs
print(get_positive([-1, 2, -4, 5, 6])) # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: [5, 3, 2, 3, 9, 123]
print(get_positive([5, '3', -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: []
print(get_positive([5, (3<<1), -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: []
```