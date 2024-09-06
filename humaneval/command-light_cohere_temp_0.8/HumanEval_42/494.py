```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i + 1 for i in l] + [n + 1]
    return result

# Test the function with sample inputs and expected outputs
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that returns a list with elements incremented by 1, and a test function `test_incr_list` to check if the function is working correctly with different inputs.  The output is the content of the incr_list function and the test function.