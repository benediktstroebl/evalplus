```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    (=[1, 2, 3], [2, 3, 4]),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10]),
    # Added an edge case with a single element
    ([10], [])
]

for case in test_incr_list:
    actual_result = incr_list(case[0])
    expected_result = case[1]
    assert actual_result == expected_result, f"Incorrect result: {actual_result}"
```
Do you want me to assist you with additional test cases or help with any other aspects of the problem?