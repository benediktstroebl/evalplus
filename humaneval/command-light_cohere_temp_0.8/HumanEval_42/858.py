```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Incorrect return"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Incorrect argument"
``` 
This script defines a function `incr_list` that returns a new list with elements incremented by 1. It also contains a test_incr_list, which tests the `incr_list` function with various inputs and ensures the correct behavior of the function.