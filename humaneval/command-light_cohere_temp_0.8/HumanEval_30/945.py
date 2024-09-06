```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = []
test_cases = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 10, 100]]

# Run the function on each test case and compare the output with expected results
for case in test_cases:
    actual_result = get_positive(case)
    expected_result = case
    test_get_positive.push(actual_result, expected_result)

# Print the results
print("Test Results:")
for item, expected in zip(test_get_positive, expected_results):
    print(f"{item} => {expected}")
```