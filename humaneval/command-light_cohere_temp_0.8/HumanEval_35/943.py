```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], None),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 5),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], -10),
    ( [], 0),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], None),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)]

for test_case, expected in test_max_element:
    actual = max_element(test_case)
    if actual != expected:
        print(f"Test case {test_case} failed with {actual} != {expected}")
```
The Python script defines a function max_element that finds the maximum element in a list. The function uses the MAX() function directly on the input list, which returns the largest element in the list.

The script also has a set of test cases, which pass through the max_element function with various lists. The function is then compared with the expected output to ensure it is working correctly.