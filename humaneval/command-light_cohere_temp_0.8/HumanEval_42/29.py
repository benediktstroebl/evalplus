```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [i+1 for i in l] + l
    return res

# Test
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    got = incr_list(lst)
    assert expected == got, "Test failed: expected {}, got {}".format(expected, got)

# Run the function and test it
test_incr_list()
```
This code defines a function `incr_list` that returns a list with elements incremented by 1, and a test function `test_incr_list` that verifies if the function behaves correctly with a given list of inputs. This script can be executed as a standalone Python file or imported as a module to be used within other scripts.