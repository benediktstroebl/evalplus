```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty")
    return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected
```
The `max_element` function in this script accepts a list `lst` as input and returns the list's highest element using the Python `max()` function. The `test_max_element` function creates a test list and runs the `max_element` function on it. The `assert` statement compares the expected results with those from `max_element`. 

This code may be executed in a Python environment or IDE to run the test suite and check the `max_element` function's correctness.