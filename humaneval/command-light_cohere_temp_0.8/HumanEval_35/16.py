```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with various lists
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
assert max_element([]) == 0
assert max_element([21, 12, 13]) == 13
assert max_element([21, 12, 34, 13]) == 34
```
The function max_element takes a list as input and uses the built-in function max to return the maximum element in the list. The test cases demonstrate the area of the function's use. The code is a best practice for self-contained functions as it is short, clear, and easy to read.