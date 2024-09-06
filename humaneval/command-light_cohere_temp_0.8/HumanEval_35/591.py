```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a list of numbers
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 123
```
This code defines a function `max_element` that returns the maximum element in the input list `l`. It utilizes the built-in `max()` function to achieve this. The test at the final line ensures that the function produces the correct result for the given input list.