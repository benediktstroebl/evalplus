```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test list input
assert max_element([1, 2, 3]) == 3
assert max_element([-5, -3, -10]) == -10
assert max_element([123, 456, 789]) == 123
```
This Python script defines a function max_element that calculates the maximum element in a given list. The function uses the method max() to find the largest element in the list.

The test section ensures the function's correctness by evaluating it with various input lists, and the assertions verify that the output matches the expected result.