```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with a sample list
test_get_positive = []
test_get_positive.push_ into_list([-1, 2, -4, 5, 6])
test_get_positive.push_into_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Call the function and verify the output
assert(test_get_positive == get_positive(test_get_positive))

# Test with a list with both positive and negative numbers
test_positive_numbers =  [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

assert(get_positive(test_positive_numbers) == test_positive_numbers)
```