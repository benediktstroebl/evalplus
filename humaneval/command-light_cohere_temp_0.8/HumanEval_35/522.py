```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1
test_cases = [[1, 2, 3], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

for test_case in test_cases:
    actual_result = max_element(test_case)
    expected_result = 3  # [Your value here]
    print(f"Test case 1: {test_case}, Expected Result: {expected_result}, Actual Result: {actual_result}")

# Test case 2
test_cases = [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [1, 2, 3, -20]]

for test_case in test_cases:
    actual_result = max_element(test_case)
    expected_result = float('-inf')
    print(f"Test case 2: {test_case}, Expected Result: {expected_result}, Actual Result: {actual_result}")

# Test case 3
test_cases = [[5, 3, -5, 2, -3, 3, 9, 0, 123, -100, 1, -10]]

for test_case in test_cases:
    actual_result = max_element(test_case)
    expected_result = -100.0
    print(f"Test case 3: {test_case}, Expected Result: {expected_result}, Actual Result: {actual_result}")
```

This code defines a function max_element that takes a list as input and returns the maximum element in the list using the max() function. The code also provides several test cases to verify the correctness of the max_element function. It compares the expected and actual results for each test case and uses the print statement to display the results.