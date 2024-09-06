```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with a list of numbers
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
 assert max_element(test_max_element) == 123
# Test the function with a list of strings
test_max_element(["A", "B", "C"])
 assert max_element(test_max_element) == "C"
```
The function max_element solves the problem of finding the maximum element in a list. It uses the max() function from Python's built-ins to return the maximum of the passed list.