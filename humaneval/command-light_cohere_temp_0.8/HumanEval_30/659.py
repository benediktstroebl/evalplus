```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test cases
test_get_positive = [
    """[-1, 2, -4, 5, 6]
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    [10, -20, 30, -40, 50]
    [True, True, False, False]
]

def test_function(test_case):
    actual_result = get_positive(test_case)
    expected_result = [num for num in test_case if num >= 0]
    assert actual_result == expected_result, f"Test case {test_case} failed"
    return actual_result

for test in test_get_positive:
    print(test_function(test))
```