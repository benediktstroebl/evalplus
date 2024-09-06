```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic positive numbers
assert max_element([1, 2, 3]) == 3

# Test case 2: Complex numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3: Mixed numbers and strings
assert max_element([5, 3, -5, 2, -3, 'abc', 3, '123']) == 3

# Test case 4: Large numbers
assert max_element([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9

# Test case 5: Negative numbers
assert max_element([5, 3, -5, 2, -3, 3, -9, 0, -123]) == -123
```
This script defines a `max_element` function that returns the maximum element in the input list. It's then used for testing different scenarios with various types of lists.