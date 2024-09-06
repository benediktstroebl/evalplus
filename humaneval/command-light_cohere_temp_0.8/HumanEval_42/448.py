```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list([]) == []
    assert incr_list([10, 100]) == [101]
    assert incr_list([2, 5, 6, 7]) == [7, 8, 9]
```
This script defines a function incr_list that adds 1 to each element of a passed list, and a test function test_incr_list that verifies the correctness of the incr_list function through a series of test cases.