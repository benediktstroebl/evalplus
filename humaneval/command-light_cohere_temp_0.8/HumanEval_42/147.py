```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert len(l) == n
    return l

# Test suite
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list(test_list) == expected

# Main function
if __name__ == "__main__":
    test_incr_list()
```
This code defines a function `incr_list` that increments every element in a given list by 1. The function is self-contained and returns a new list with the updated values. 

Additionally, a test suite is provided to ensure the correctness of the `incr_list` function by checking if the returned list matches the expected result.