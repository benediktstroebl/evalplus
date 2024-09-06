```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with some data
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_positive = get_positive(test_data)
print(test_positive)  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```