```python
def sort_even(lst):
    return lst[:] if all(i % 2 == 0 for i in lst) else lst

# Test case 1:
assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2:
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Test case 3:
assert sort_even([5, 6, 7]) == [5, 6, 7]

# Test case 4:
assert sort_even([2, 4, 8, 10]) == [4, 8, 10, 2]

# Test case 5:
assert sort_even([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test case 6:
assert sort_even([-1, -2, -3, -4]) == [-1, -2, -3, -4]
```