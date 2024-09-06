```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.push_back([-1, 2, -4, 5, 6])
test_get_positive.push_back([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Call the function and verify the output
print(get_positive(test_get_positive))
```