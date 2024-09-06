```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test cases
test_get_positive = [
    [],
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for test_case in test_get_positive:
    actual_result = get_positive(test_case)
    expected_result = test_case
    assert actual_result == expected_result, f"Test case [{test_case}] failed."
```