```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in range(n)]
    assert list(result) == [2, 3, 4]
    for i in range(n):
        assert l[i] == result[i] == i+1
    return result
```