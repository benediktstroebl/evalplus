```python
def max_element(lst):
    return max(lst)

# Test the function with various lists
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([]) == float('-inf')
assert max_element([10, 1, 10]) == 10

```
This script defines a function `max_element` that takes a list as an argument and returns the maximum element in that list. 

The test cases ensure the function works correctly with different types of lists and empty lists.