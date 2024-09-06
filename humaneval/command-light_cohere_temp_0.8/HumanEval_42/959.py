```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1): result[i] = l[i-1] + 1
    return result
 
def test_incr_list():
    """Function to test the incr_list function."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    result = incr_list(lst)
    assert expected == result, "Incral list does not return expected output."
```