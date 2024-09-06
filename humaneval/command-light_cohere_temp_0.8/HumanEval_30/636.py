```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.add([list([-1, 2, -4, 5, 6])]
test_get_positive.add([list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

assert get_positive(test_get_positive) == [2, 5, 6, 3, 9, 123, 1]
```