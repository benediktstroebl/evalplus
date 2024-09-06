```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test the function
def test_incr_list():
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    actual = incr_list(lst)
    assert actual == expected
```