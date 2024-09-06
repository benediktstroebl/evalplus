```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with a variety of data
test_get_positive = []
test_get_positive.push_into_list([
    [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]])

# Verify the function's output
test_get_positive = [test_get_positive[0], test_get_positive[1]]
print(get_positive(test_get_positive))  # Expected: [2, 5, 6]
print(test_get_positive[0] == get_positive(test_get_positive)) # True, all numbers are returned
```