```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(result[i] == i+1 for i in range(n))
    return result
# Test the function
test_list = [5, 3, 5, 2, 3, 3]
test_result = incr_list(test_list)
assert test_result == [6, 4, 6, 3, 4, 4]
test_list2 = [5, 3, 5, 2, 3, 9, 0, 123]
test_result2 = incr_list(test_list2)
assert test_result2 == [6, 4, 6, 3, 4, 4, 10]
```