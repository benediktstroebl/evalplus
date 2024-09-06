```python
def incr_list(lst):
    new_val = lst[-1] + 1
    return [new_val] + lst[:-1]

# Test
def test_incr_list():
    assert list(incr_list([1, 2, 3])) == [2, 3, 4]
    assert list(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```