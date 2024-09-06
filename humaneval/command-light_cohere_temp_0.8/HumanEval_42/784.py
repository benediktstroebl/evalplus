```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    assert len(l) == n
    assert all(x + 1 == l[i] for i, x in enumerate(l))
    return l

# Test cases
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test_incr_list()
```

The function `incr_list` generates a new list with elements increased by 1, and the test cases validate the expected behavior of the function with various input lists.  The test_incr_list() function will run the test cases to verify the correctness of the `incr_list` function.