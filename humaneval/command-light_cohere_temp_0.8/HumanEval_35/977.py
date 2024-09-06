```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
assert max_element([-5, 3, -2, -3, 8, -11]) == -3

# Test case 3
assert max_element([1, 2, 3, -5, 4, -6, -7]) == -7

# Test case 4
assert max_element([10, 2, 3, -4, 5]) == 5
```
The code defines a function `max_element` that computes the maximum element within a given list. The test cases ensure that the code provides the correct maximum element for the corresponding lists.