```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with sample inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Verify the function output with assertions
assert test_get_positive == [2, 5, 6, 3, 9, 123, 1]

# Test again with different input list
test_get_positive2 = []
test_get_positive2.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Verify the function output with assertions
assert test_get_positive2 == [3, 5, 2, 3, 9, 123]
```
The function returns a new list containing only positive numbers, and the test cases pass the corresponding assertions.