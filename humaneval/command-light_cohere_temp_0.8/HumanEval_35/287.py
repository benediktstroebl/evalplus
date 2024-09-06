```python
def max_element(lst):
    return max(lst)

# Test the function with a list of numbers
test_result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_result == 123

# Test the function with a list of strings
test_result2 = max_element(['abc', 'def', '123', '456'])
assert test_result2 == 456
```
This script defines a function `max_element` that calculates and returns the maximum element from the input list `lst`. The function is then tested with two different lists, and the results are compared to expected maximum element values.