```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = [
    ("[-5, 3, 2, -3, 3, 9, 0, 123, 1, -10, 5]", None),
    ("[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]", 5),
    ("[-5, -10, 2, -3, 3, 9, 0, 123]", -5),
    ("[1, 2, 3, -20, -40, 80]", None),
    # Add more test cases as needed
]

for test_case, expected in test_max_element:
    actual = max_element(test_case)
    if actual != expected:
        print(f"Test case {test_case} failed. The expected maximum is maximum element is {expected}, but got {actual}")
```
The provided Python script defines a function max_element that computes and returns the maximum element from a given list. It also includes a test suite, consisting of a collection of input test cases and their corresponding expected maximum element values. The script then iterates through the test cases, applying the max_element function and comparing its output with the expected results. If there's expected results match, the test passes successfully.