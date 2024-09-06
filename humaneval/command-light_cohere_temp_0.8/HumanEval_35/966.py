```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with various input lists
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([-5, -3, -10]) == -10
assert max_element([1, 2, -5, -10, -3]) == -3
assert max_element([]) == 0
assert max_element([1, 2, 3, 4, 5]) == 5
```
This code defines a function max_element that returns the maximum element in a given list. 

Then, the code provides several test cases to validate the correctness of the max_element function.