```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test function
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    for x, y in zip(test_list, expected):
        assert x == y, f"ERROR at index {x} : Expected {y}, Got {x}."

# Main execution
test_incr_list()
``` 
This script defines the `incr_list` function that takes a list `l` and returns a new list with each element from `l` incremented by 1. The `test_incr_list` function is used to test the `incr_list` function with a sample input list, and the results are compared to the expected output. 
Finally, the `test_incr_list` function is called to run the tests.