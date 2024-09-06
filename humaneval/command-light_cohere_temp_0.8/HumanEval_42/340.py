```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst[::i] = lst[:] + [1]
    return lst

# Unit tests
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    return True

# Main function to run the tests
if __name__ == "__main__":
    test_incr_list()
``` 
This code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. It also includes a test_incr_list, which verifies the correctness of the `incr_list` function by testing its output against the expected results for specific input lists. The `main` function is responsible for running the tests.