```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with various list inputs
# Test with lists containing only positive numbers
test_get_positive([1, 2, 3, 4, 5])
test_get_positive([-1, 2, -4, 5])
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1])
test_get_positive([-10])
# Test with lists containing both positive and negative numbers
test_get_positive([-1, 2, -3, 4, 5, 6])
test_get_positive([0, 2, 3, -10])
```