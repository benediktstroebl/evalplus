```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some examples
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The given Python function `max_element` takes a single argument `l`, which is expected to be an iterable or a list. The function then uses the max() function to find the maximum element in the list and returns its value. 

The `assert` statement is used to test the correctness of the `max_element` function by comparing the result with the expected maximum element.