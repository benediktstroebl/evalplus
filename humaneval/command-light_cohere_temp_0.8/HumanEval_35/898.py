```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with various inputs
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123)

# Test with an empty list
assert(max_element([]) == None)

# Test with list of strings
assert(max_element(["A", "B", "C"]) == "A")

# Test with custom function
assert(max_element(math_factorial)) == 60
```
The script defines a function max_element that takes a list as input and returns the maximum element in that list. It is then passed various tests to ensure its correctness.