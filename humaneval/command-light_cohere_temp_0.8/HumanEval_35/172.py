```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123  # Pass

# Run the function
test_max_element()
``` 
This code defines a Python function `max_element(lst)` that calculates and returns the maximum element from the input list `lst`. It also includes a test function `test_max_element()` that creates a test list and asserts that the `max_element()` function returns the correct maximum element value when applied to the test list.  Finally, the function is then called from the `test_max_element()` function, which passes the test and demonstrates that the function is working correctly.