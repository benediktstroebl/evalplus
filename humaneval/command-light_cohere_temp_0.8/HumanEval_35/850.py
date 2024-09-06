```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function
def test_max_element():
    assert max_element([1, 2, 3]) == 3

# Test with list of numbers and string
assert max_element([5, 3, -5, 2, -3, 3, 'hello']) == 3

# Test with invalid input
try:
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, '123']) == 123  # This should raise an AssertionError
except AssertionError:
    print("Error: Test case failed")

```  The `max_element` function takes a single argument, `l`, which is a list. The function returns the maximum element in the list, which is determined using the `max()` function. The function is then tested using various test cases. 

You can use this function to find the maximum element in any list.