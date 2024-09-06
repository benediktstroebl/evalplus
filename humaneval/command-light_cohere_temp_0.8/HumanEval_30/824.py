```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with different lists of numbers
test_get_positive_list([-1, 2, -4, 5, 6])
test_get_positive_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```