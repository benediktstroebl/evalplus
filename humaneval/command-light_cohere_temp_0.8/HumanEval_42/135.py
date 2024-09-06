```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    l[:] = [i+1 for i in l]
    return l

# Test suite
def test_incr_list():
    tests = [
        ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]),
        ([], ['a']),
        ([100], ['1', '2', '3']),
        ([], [1, 2, 3, 'a'])
    ]
    assert incr_list(tests[0]) == [2, 3, 4]
    assert incr_list(tests[1]) == [6, 4, 6, 3, 4]
    assert incr_list(tests[2]) == [6, 4, 6]
    assert incr_list(tests[3]) == [6, 4, 6, 'a'] == 'aaaa'
    assert incr_list(tests[4]) == [6, 4, 6, 1] == '123456'
    assert incr_list(None) is None
```