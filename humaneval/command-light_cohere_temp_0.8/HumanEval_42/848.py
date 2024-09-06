```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    return result[:n]

# Test function to check if incr_list works correctly
def test_incr_list():
    assert list(incr_list([1, 2, 3])) == [2, 3, 4]
    assert list(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```  The provided test function 'test_incr_list()' checks if the 'incr_list()' function works as expected by comparing the output of the function with the expected output.