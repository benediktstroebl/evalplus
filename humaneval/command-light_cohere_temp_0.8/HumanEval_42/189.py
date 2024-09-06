```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function
def test_incr_list():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    got = incr_list(test_list)
    assert expected == got
```