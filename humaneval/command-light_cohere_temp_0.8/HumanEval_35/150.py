```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], None),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 3),
    ( [-10, -20, -30, -40], None),
    ( [], None),
    ( [1, 2, 3, -4], 3),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -5),
]

for test_case, expected_result in test_max_element:
    actual_result = max_element(test_case)
    if actual_result != expected_result:
        print(f"Test case {test_case} failed: actual {actual_result}, expected {expected_result}")
```