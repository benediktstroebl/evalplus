```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1
test_suite = [get_positive([-1, 2, -4, 5, 6])]
assert test_suite == [2, 5, 6]

# Test case 2
test_suite = [get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])]
assert test_suite == [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (bad input)
test_suite = [get_positive([5, 3, -5, 2, -3, 3, 9, 0, b, 1])]
with pytest. assertanfinput raises(ValueError, "Input list is not iterable"))
```