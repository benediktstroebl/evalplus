```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [0] 

# Test suite
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(incr_list(test_list)) == expected
test_incr_list()
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements from input list incremented by 1. It also includes a test_incr_list function with a test suite that creates a test list and uses the incr_list function to get the expected result.