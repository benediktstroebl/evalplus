```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """
    Test incr_list function
    """
    # Test list with elements 5, 3, 5, 2, 3, 3, 9, 0, 123
    assert incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])) == 16 
# Main execution 
if __name__ == "__main__":
    test_incr_list()
``` 
The provided solution is a Python function `incr_list` that takes a single argument, a list, and returns a new list with elements incremented by 1. The test function `test_incr_list` is designed to test the `incr_list` function with a variety of input lists. 

To execute the script, we use the `if __name__ == "__main__":` block to verify that the code is run when executed as the main script, not when imported as a module.