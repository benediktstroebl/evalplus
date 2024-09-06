```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Function to test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Failed to increment elements"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Failed to increment elements"
``` 
This script defines a function `incr_list` that adds 1 to each element in a given list, and passes the test with test_incr_list, which checks if the result is correct.