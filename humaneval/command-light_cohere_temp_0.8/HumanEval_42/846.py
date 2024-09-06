```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Test incr_list function."""
    lst = [1, 2, 3]
    assert lst == incr_list(lst)

def test_incr_list_again():
    """Test incr_list function again."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert lst == incr_list(lst)

# Main function to run the tests.

if __name__ == "__main__":
    test_incr_list()
    test_incr_list_again()
``` 
This script defines the function `incr_list` that simply returns a list with elements incremented by 1. The `test_incr_list` function tests the `incr_list` function by creating a list and asserting that it is equal to the result of `incr_list`. The `test_incr_list_again` function tests the `incr_list` function again using a different list.  Finally, the main function is used to run the test functions, which will check that the `incr_list` function is working correctly.