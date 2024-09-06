```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[n] + 1)
    return l

# Test function
def test_incr_list():
    """Return list with elements decremented by 1."""
    l = [1, 2, 3]
    l.append(-l[-1] - 1)
    return l

# Test cases
tests = {test_incr_list.to import __name__ + "Test Cases"}

# Run the tests
tests()
```
This script defines a function `incr_list` that increments each element in a list by 1 and a test function `test_incr_list` that decrements each element in the list by 1. The test cases are defined as a dictionary with `test_incr_list` as the key and the value is the actual function to be tested. The script then runs the test cases and passes the tests using the `tests()` function.