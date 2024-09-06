```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Failed to increment elements correctly."

# Run the tests when the script is executed without any arguments
test_incr_list()
```
The code provides a function `incr_list` that takes an input list and returns a new list with elements incremented by 1. The `test_incr_list` function is used to test the `incr_list` function with a simple input list, and the test passes, so the function works as expected.