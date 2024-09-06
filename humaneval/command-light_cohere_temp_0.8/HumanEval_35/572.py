```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 ( Corner case: List with only one element )
assert max_element([9]) == 9

# Test case 4 ( Empty list )
assert max_element([]) is None

# Test case 5 ( List with negative numbers )
assert max_element([5, -5]) == 5
```
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. This is then by using the `max` function from the Python standard library to find the maximum value in the list. The test cases provided are designed to cover a range of scenarios and ensure that the function works correctly.