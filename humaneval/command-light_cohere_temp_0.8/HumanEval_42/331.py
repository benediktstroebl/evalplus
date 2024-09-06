```python
def incr_list(lst):
    lst[0] += 1
    for i in lst[1:]:  lst[i] += 1
    return lst

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([100, 200, 300]))) == 3
    assert incr_list([]) == []
```
This script defines a function `incr_list` that incrementally every element in a given list by 1, then returns the updated list. It also has a test suite with several test cases, which verify the correctness of the `incr_list` function.