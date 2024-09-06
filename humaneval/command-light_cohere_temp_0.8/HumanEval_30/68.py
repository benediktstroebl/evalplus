```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.add([range(1, 6))
test_get_positive.add([range(-1, 0, -5))
test_get_positive.add([range(0, 1, -3, 2, -9, -5))

print(get_positive(test_get_positive))
```