```python
def max_element(lst):
    if not_input(lst):  # Test for empty list
        return None
    max_num = max(lst)
    return max_num

def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    assert max_element(lst) == expected

def test_output():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    result = max_element(lst)
    assert result == 10
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. The `test_max_element` function tests the `max_element` function by providing an input list and an expected maximum element, and `test_output` runs additional tests to ensure the function behaves correctly.