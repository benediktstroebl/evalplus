```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123  # Passes

# Run the function and test it
max_element(test_list)
test_max_element()
```  This code defines a function `max_element` that takes a list as input and returns the maximum element in the list. Additionally, the code includes a test function `test_max_element` to verify the correctness of the `max_element` function.  The runs the also the function and test to ensure that it is working correctly.