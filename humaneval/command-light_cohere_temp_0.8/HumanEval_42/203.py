```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [x+1 for x in l]
    assert len(result) == n
    assert all(result[i] == i+1 for i in range(n))
    return result

# Test the function with known correct results
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```