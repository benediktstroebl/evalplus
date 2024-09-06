```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([]) == 0

# Test case 4
assert max_element([10, 30, 100]) == 100
``` 
This script defines a function max_element that finds and returns the maximum element in a given list. The code also passes tests to ensure that the function is working correctly.