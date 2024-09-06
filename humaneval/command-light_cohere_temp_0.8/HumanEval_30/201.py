```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test cases
test_get_positive = []
test_cases = [
    [],  # List of values
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for test_case in test_cases:
    actual_result = get_positive(test_case)
    expected_result = [2, 5, 6]
    assert actual_result == expected_result, f"Incorrect result for {test_case} - got {actual_result} but expected {expected_result}"

# Main function call
```