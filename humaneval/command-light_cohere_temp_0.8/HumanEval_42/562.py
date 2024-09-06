```python
def incr_list(lst):
    lst[::] = lst[-1] + 1
    return lst

# Test cases for incr_list function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This code defines a function incr_list that returns a new list with the last element of the input list incremented by 1. It also includes a test_incr_list function with assert statements that check the correctness of the incr_list function with different input lists.