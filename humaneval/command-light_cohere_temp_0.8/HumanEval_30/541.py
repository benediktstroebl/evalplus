```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.py  = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

for test_lst in test_get_positive:
    actual_result = get_positive(test_lst)
    expected_result = [2, 5, 6, 5, 3, 9, 123, 1]
    assert actual_result == expected_result, f"Test {test_lst} failed"
```  The `get_positive` function returns only the positive numbers from the input list.