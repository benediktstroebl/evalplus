```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function
def test_incr_list():
    test_list = [1, 2, 3]
    result = incr_list(test_list)
    assert result == [2, 3, 4]
    test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result2 = incr_list(test_list2)
    assert result2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```