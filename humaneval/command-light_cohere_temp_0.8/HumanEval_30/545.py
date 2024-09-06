```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with a list of different numbers
test_get_positive = []
test_get_positive.push_or_int([-1, 2, -4, 5, 6])
test_get_positive.push_or_int([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Call the function and store the result in the same list
test_get_positive.push_or_int([x for x in test_get_positive])

# Print the result
print(test_get_positive)
```