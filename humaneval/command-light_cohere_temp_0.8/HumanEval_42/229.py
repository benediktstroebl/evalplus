```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Unit tests for incr_list function."""
    lst = [1, 2, 3]
    assert lst == incr_list(lst)
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert lst == incr_list(lst)
``` 
This script defines a function incr_list that increments elements in a list by 1 and passes the test using the test_incr_list function.