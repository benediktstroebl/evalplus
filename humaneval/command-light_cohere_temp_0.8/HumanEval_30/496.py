```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
test_get_positive = []
test_get_positive.add([range(1,6))
test_get_positive.add([range(-1, -5))
test_get_positive.add([range(0, 10))

print(get_positive(test_get_positive)) # Output: [1, 2, 3, 5, 6]
```