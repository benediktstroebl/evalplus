```python
def max_element(lst):
    return max(lst)

# Test cases
test_cases = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [-2, -3, -4, -5, -6, -7, -8, -9],
    [10, 11, 12, 13]
]

for test_case in test_cases:
    actual_result = max_element(test_case)
    expected_result = max(test_case)
    print(f"Test case {test_case} : Expected {expected_result}, Actual {actual_result}")
    assert actual_result == expected_result
```