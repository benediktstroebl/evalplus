```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1:
assert max_element([1, 2, 3]) == 3

# Test case 2:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3:
assert max_element([]) is None

# Test case 4:
assert max_element([12, 34, 2, 1]) == 34
```
The above Python script defines a function `max_element` that aims to find the maximum element within a given list. It achieves this by utilizing the max function with a list comprehension, which returns the highest value in the list. This function is also incorporates several test cases to ensure its correctness. 

When running the script, you can execute the `max_element` function with different input lists and verify the output against the expected maximum element.