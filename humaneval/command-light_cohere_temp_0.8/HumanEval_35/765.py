```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], lambda x: x),
    ( [5, 3, -5, 2, -3], None),
    # Edge case: [-100, -1, 0]
    ([-100, -1, 0], lambda x: x),
    # Multi-element list
    ([1, 2, 3, 4, 5, 6], None),
]

for test_case in test_max_element:
    actual_result = max_element(test_case[0])
    expected_result = test_case[1]
    if actual_result is not expected_result:
        raise ValueError("Test case failed: {}".format(test_case))

print("All test cases passed!")
```