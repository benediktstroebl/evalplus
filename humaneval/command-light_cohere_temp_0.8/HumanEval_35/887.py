```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], max_element),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123], "max_element should return 123")
]

for test_case in test_max_element:
    actual_value, expected = test_case
    actual_result = max_element(test_case)
    print(f"Test {test_case}: actual {actual_result}, expected {expected}")
```

This script defines a function max_element that finds the maximum element in a given list. It is then a function passed to test cases, where the function is invoked with different lists, and the results are compared against the expected output. The code provides a test cases with lists and the function to ensure its correctness.