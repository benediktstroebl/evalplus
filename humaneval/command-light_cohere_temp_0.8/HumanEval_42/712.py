```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * n
    result[0] = l[0]
    for i in range(1, n):
        result[i] = l[i-1] + 1
    return result
 
#Test suite for incr_list function
def test_incr_list():
    test_list = [5, 3, 2, 1]
    expected = [6, 4, 3, 2]
    result = incr_list(test_list)
    assert expected == result
    test_list = [5, 3, 5, 2, 3]
    expected = [7, 5, 6, 3]
    result = incr_list(test_list)
    assert expected == result
```