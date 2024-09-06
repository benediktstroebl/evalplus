```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [i + 1 for i in l]
    return new_list

# Test function for incr_list
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(test_list)
    assert result == [6, 3, 6, 4, 6, 4, 10, 1, 124]

# Driver code
test_incr_list()
``` 
This code defines a function incr_list that adds a incrementing value to each element in a given list. The test_incr_list function tests the incr_list function with a sample input list and checks if the result matches the expected output. The driver code then creates the test list and calls the test_incr_list function to run the tests.