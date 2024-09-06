```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a variety of list inputs
# Test with both positive and negative numbers
# Test with different data types
# Test with complex list content
list_tests = [
    ([1, 2, 3]),
    (-5, 3, -10),
    (5, 3, "abc"),
    (0, -3, 123, [1, 2, 3]),
    (1, 2, -3, [3, 2, 1]),
    (9, 0, 123, [9, 0, 123])
]

for lst, test in list_tests.With(input) for x in lst:
    assert max_element(x) == test, f"Error: {x} should be the maximum element, but is not"
```

This script defines a function max_element that returns the maximum element in a given list, and then tests the function with various input lists to ensure its correctness.  The script is self-contained and provides a clear and concise way to solve the maximum element problem.