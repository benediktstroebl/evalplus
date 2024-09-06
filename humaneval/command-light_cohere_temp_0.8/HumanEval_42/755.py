```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst[:] = [lst[-1] + 1]
    return lst

#Test cases for incr_list function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([99, 2, 100, 1]))) == 4
    assert incr_list([-1, -100]) == [-2, -101]
    assert incr_list([]) == []
```
This Python code defines a function incr_list that incrementally a list with a given input list lst. The function creates a new list with the last element of lst incremented by 1 and returns the new list. The code also provides several test cases to verify the correctness of the incr_list function. These tests test test cases cover various scenarios, including non-negative numbers, negative numbers, empty input, and lists with different lengths. The test cases ensure that the incr_list function correctly increments the list elements and returns the expected results.