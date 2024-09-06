```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with some data
test_data = [
    -1, 2, -4, 5, 6, 7, -5, 3, 0, 123, 1, -10
]
result = get_positive(test_data)
assert result == [2, 5, 6, 3, 9, 123, 1]

# To change the function and test data, modify this section
```