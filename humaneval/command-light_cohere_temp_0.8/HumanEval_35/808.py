```python
def max_element(lst):
    return max(lst)

# Basic test case using built-in list
assert max_element([1, 2, 3]) == 3

# Test case with existing max element
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case with negative elements
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == -10

# Test case with complex list
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, -100]) == -100
```
This code defines a function max_element that calculates and returns the maximum element in a given list. It is also includes various test cases to validate the correctness of the max_element function for different scenarios.