```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = [
    ("[-1, 2, -4, 5, 6]", [2, 5, 6]),
    ("[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]", [5, 3, 2, 3, 9, 123, 1])
]

# Function test
def test_function(test_case):
    actual_result = get_positive(test_case)
    expected_result = test_case[1]
    assert actual_result == expected_result, f"AssertionError: {test_case[0]} != {expected_result}"

# Run the test
test_get_positive_result = all(test_function(test) for test in test_get_positive)
print("Test Results:", test_get_positive_result)
```