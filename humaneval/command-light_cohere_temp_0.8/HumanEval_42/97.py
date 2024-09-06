```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Function to test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4], "List not incremented correctly"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "List not incremented correctly" 
# Run the test function to check the implementation
test_incr_list()
```

The code defines a function `incr_list` that returns a list with elements incremented by 1. The `test_incr_list` function tests the `incr_list` function by asserting that its output is correct for a given input list. 

This self-contained Python script demonstrates the concept of functional testing and provides a function that can be used to create a list with elements incremented by 1.