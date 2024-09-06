```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.add([range(0, 6))
test_get_positive.add([range(1, 4))
test_get_positive.add([range(5, 100))

# Function call and test
assert get_positive(test_get_positive) == [2, 3, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```