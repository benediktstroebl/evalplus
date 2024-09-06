```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Test function for incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Failed test 1"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Failed test 2"
    return "Test passed"

# Call test function to see if it passes
print(test_incr_list())
 ``` 
This script defines a function incr_list that adds 1 to each element in the input list and passes the test function test_incr_list that checks if the result is correct. 

The code is well-structured and follows good practices.