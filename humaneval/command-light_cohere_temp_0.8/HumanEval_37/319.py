```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [x for x in lst[0] if x % 2 != 0]]

# Test the function with different lists
assert(sort_even([1, 2, 3]) == [1, 2, 3])
assert(sort_even([5, 6, 3, 4]) == [3, 6, 5, 4])
assert(sort_even([10, 20, 30]) == [10, 20, 30])
```