```python
def incr_list(lst):
    n = len(lst)
    result = [i + 1 for i in range(n)]
    return result

# Test
def test_incr_list():
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    got = incr_list(lst)
    assert list(got) == expected
```