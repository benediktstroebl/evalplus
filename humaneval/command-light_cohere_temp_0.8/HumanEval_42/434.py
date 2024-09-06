```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with known good inputs
def test_incr_list():
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(lst)
    assert result == expected
```
The function incr_list builds a list with elements incremented by 1 and tests the function with a known good input.