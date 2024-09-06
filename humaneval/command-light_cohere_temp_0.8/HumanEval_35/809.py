```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = [
    ("[-5, 3, 2], "[-5, 3, 2]"),
    ("[-5, 3, 2, -5, -3, 3, 9, 0, 1, -10]", "[-5, 3, 2, -5, -3, 3, 9, 0, 1, -10]"),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], "MAX_ELEMENT"),
]

for test in test_max_element:
    assert max_element(test[0]) == test[1], f"Error: {test[1]} != MAX_ELEMNT"
```
This Python script defines a function `max_element` that returns the maximum element in the input list. The script also includes a set of test cases to verify the correctness of the function, it asserts that the output of `max_element` with the input list matches the expected output from the test case.