```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    [list([-1, 2, -4, 5, 6])],
    [2, 5, 6],
]

# Execute the function and compare the results
for test_case in test_get_positive:
    actual_result = get_positive(test_case[0])
    assert actual_result == test_case[1], "Test case failed: " + str(test_case) + '"
```