```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test the function with known good inputs
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The `incr_list` function takes a list `l` as input and returns a new list with elements from input list incremented by 1. The `test_incr_list` function tests the `incr_list` function with some known good inputs and asserts that the function returns the correct result. 
This script is self-contained, and you can use the `incr_list` function and `test_incr_list` function to solve the problem and verify the results without using external libraries or modules.