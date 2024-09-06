```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l

def test_incr_list():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    actual = incr_list(l)
    assert l == expected
    assert len(l) == len(expected)

# Run the tests
test_incr_list()
```
This code defines a function `incr_list` that appends 1 to each element of a given list, and a test function `test_incr_list` that verifies that the `incr_list` function operates correctly by comparing the original list with the expected list, and checking the length of both.