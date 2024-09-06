```python
def sort_even(lst):
    return lst[:] if any(x % 2 == 0 for x in lst) else lst[:] + [x for x in lst if x % 2 != 0]

# Tests
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
assert sort_even([8, 9, 4, 7]) == [4, 7, 8, 9]
assert sort_even([11, 22, 11, 33]) == [11, 11, 22, 33]
```