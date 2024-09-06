```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123

# Run the test
test_max_element()
 ```