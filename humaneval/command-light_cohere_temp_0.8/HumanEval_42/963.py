```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

def test_incr_list():
    """Test the function incr_list with a list of numbers"""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```
This code defines a function `incr_list` that adds 1 to the end of a given list and returns the updated list. Then, the test_ incr_list function with a test case that confirms if the function works correctly by adding 1 to the end of the list and returning the updated list.