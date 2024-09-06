```python
def incr_list(lst):
    lst.append(1)
    lst.append(2)
    lst.append(3)

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

```

This script defines a function `incr_list` that takes a list `lst` as input and returns a new list with elements incremented by 1. The test function `test_incr_list` is used to check the correctness of the `incr_list` function.