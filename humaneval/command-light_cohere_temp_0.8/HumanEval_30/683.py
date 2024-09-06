```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with different input
test_get_positive = get_positive([-1, 2, -4, 5, 6])
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(test_get_positive)
 ```