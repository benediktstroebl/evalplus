```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test large input
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```
The code defines a function **incr_list** that takes a list as an argument and returns a new list with the elements incremented by 1. The test function **test_incr_list** asserts that the **incr_list** function correctly increments the elements of the input list.