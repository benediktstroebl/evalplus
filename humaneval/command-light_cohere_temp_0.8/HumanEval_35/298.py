```python
def max_element(lst):
    return max(lst)

# Test case 1:
assert max_element([1, 2, 3]) == 3

# Test case 2:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3:
assert max_element([-5, -3, -2, -3, -10]) == -3

# Test case 4:
assert max_element([1, 2, 3, 4, 5]) == 5

# Test case 5:
actual = max_element([])
expected = float('-inf')
assert actual == expected
```
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. It utilizes the maximum function to find the maximum value.

The test cases are added to ensure that the function works correctly with different lists. 

Remember to adjust the test cases to match your specific requirements.