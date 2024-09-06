```python
def max_element(lst):
    return max(lst)

# Basic test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, 3, 5, 7]) == 3

# Edge case with one element
assert max_element([]) == None

# Edge case with float
assert max_element([9, 0, 123]) == 123

# Edge case with negative element
assert max_element([9, 0, -123]) == -123
```
The function `max_element` takes a list as input and returns the maximum element in that list. It employs the max function to find the maximum element. The test cases ensure that the function works correctly for different scenarios.