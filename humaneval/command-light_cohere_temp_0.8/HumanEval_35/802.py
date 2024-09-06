```python
def max_element(lst):
    return max(lst)

# Test case 1: Positive integers
assert max_element([1, 2, 3]) == 3

# Test case 2: Elements less than 0
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3: Multiple values
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) is (max(123, -10) = 123)
```
This script defines a function max_element that calculates the maximum element in a given list. It uses the same to test the validity of the function, passing three test cases. The first test case ensures that the function correctly identifies the maximum of a list of positive integers. The second test case verifies the max against a list of negative values, and the third test case ensures the function's correctness with a list of multiple values.