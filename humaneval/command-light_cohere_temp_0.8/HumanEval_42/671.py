```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst[:] += [1]
    return lst

# Test function for incr_list
def test_incr_list(test_case):
    assert list(test_case) == [2, 3, 4]   # Should be [1, 2, 3, 4]
    assert test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]   # Should be [6,4,6,3,4,4,10,1,124]

# Driver code
if __name__ == "__main__":
    test_incr_list([1, 2, 3])  # Test with base list [1, 2, 3]
    test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])  # Test with base list [5,3,5,2,3,3,3,9,0,123]
```

This script defines a function `incr_list` that increments the elements of a list by 1 and provides a test function `test_incr_list` to check the correctness of the function. The driver code demonstrates theed using the list `[1, 2, 3]` and another list `[5, 3, 5, 2, 3, 3, 9, 0, 123]` to test the `incr_list` function.