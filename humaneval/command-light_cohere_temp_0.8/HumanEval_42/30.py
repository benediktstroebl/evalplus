```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in range(n)]
    return result

# Test case 1
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list(test_list) == expected

# Test case 2
def test_incr_list2():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    assert incr_list(test_list) == expected
```
This code provides a function incr_list that takes in a list and returns a new list with elements incremented by 1. It also includes two test cases that validate the functionality of the incr_list function with different input lists.