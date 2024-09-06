```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with sample inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Verify function output with assert
assert test_get_positive == [2, 5, 6, 3, 9, 123, 1]

# Test with another list
test_another = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert list(get_positive(test_another)) == [5, 3, 2, 3, 9, 123, 1]
```