```python
def incr_list(lst):
    lst[::] += 1
    return lst

# Test the incr_list function
test_incr_list = [
    assert incr_list([1, 2, 3]) == [2, 3, 4], "list should be incremented"
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "list should be incremented with nested items"
]
```