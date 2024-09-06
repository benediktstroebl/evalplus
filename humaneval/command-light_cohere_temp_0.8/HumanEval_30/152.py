```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with different input
# Test with list containing only positive numbers
test_get_positive([1, 2, 3, 4, 5])
assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test with list containing only negative numbers
test_get_positive([-1, 2, -3, -4])
assert get_positive([-1, 2, -3, -4]) == [-1, 2, -3, -4]

# Test with mixed positive and negative numbers
test_get_positive([-5, 2, 3, -4, -1])
assert get_positive([-5, 2, 3, -4, -1]) == [-5, 2, 3, -1]

```