```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    return l

# Test function to verify the correctness of incr_list
def test_incr_list():
    """Return list with elements decremented by 1."""
    l = [1, 2, 3]
    result = incr_list(l)
    expected = [0, 1, 2]
    assert result == expected, "Incorrect result"

# Test case with list of numbers
test_incr_list()

# Test case with list of strings
test_incr_list(["a", "b", "c"])
```

The above Python script provides a self-contained function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test function `test_incr_list` is provided to verify the correctness of the `incr_list` function by checking if its output matches the expected result. 

Additionally, two test cases are provided to demonstrate how the `incr_list` function can be used for different types of lists: