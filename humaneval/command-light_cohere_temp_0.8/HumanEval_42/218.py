```python
def incr_list(lst):
    return [lst[-1]+1, lst[-2]+1, lst[-3]+1] 

# Test function that checks if the returned list is a valid incr_list function output
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([5, 3, 'x', 4, 3])  # Missing element test
    assert not incr_list([])  # Empty list test

# Main function to call the test function
test_incr_list()

```
This Python code defines a function `incr_list` that increments the last, second to last, and third elements of a given list by 1, and a test function `test_incr_list` that checks if the `incr_list` function produces the correct output for a given list.  The finally, the `test_incr_list` function is called, which checks the function's output for various inputs.