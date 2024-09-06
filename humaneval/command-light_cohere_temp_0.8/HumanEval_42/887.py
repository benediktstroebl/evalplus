```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l = list(l)  # Convert list to mutable Python list
    return [item + 1 for item in l]

# Unit tests
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(incr_list(test_list)) == expected, "Test 1 failed"

test_incr_list()
```
This script provides a function `incr_list` that adds 1 to each element in a passed list, and a test function `test_incr_list` that checks if the function behaves as expected by comparing the output with the expected results.  It can also be used to solve this problem and ensure the correctness of the function.