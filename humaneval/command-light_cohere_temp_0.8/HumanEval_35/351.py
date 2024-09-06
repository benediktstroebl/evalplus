```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif not_empty(lst):
        return lst[0]
    else:
        max_val = max(lst)
        return max_val

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    result = max_element(test_list)
    assert result == expected, f"Expected: {expected}, Got: {result}"

def not_positive(lst):
    return all(x > 0 for x in lst)

def not_empty(lst):
    return len(lst) == 0

test_cases = {
    'Positive Numbers': [1, 2, 3, 4, 5],
    'Empty List': [],
    'Negative Numbers': [-1, -2, -3],
    'Mixed Positive and Negative Numbers': [1, 2, 3, -4, 4],
    'Ensure Empty List Outputs Are Zero': [0]
}

for test_name, test_list in test_cases.test_max_element():
    assert max_element(test_list) == test_list[0], f"Test: {test_name}, Expected: {test_list[0]}, Actual: {max_element(test_list)}"

```

This script defines a function `max_element` that calculates the maximum element in a given list. The function is tested with several test cases to ensure its correctness. The function also has helper functions to check for positive numbers, empty lists, and provide output validation.