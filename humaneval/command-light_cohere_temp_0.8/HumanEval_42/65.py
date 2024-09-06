```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test cases
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 20, 30])) == 3
    assert sorted(incr_list([1, 2, 3, 4, 5, 6]))) == [1, 2, 3, 4, 5, 6]

#main function
if __name__ == "__main__":
    test_incr_list()
```
The above Python code defines a function `incr_list` that takes a list l as input and returns a new list with elements from the original list incremented by 1. The test suite `test_incr_list` tests the `incr_list` function with various input lists, asserting the returned lists are correct. The main function is used to run the test suite when the script is executed.