```python
def incr_list(lst):
    return [lst[i]+1 for i, x in enumerate(lst)]

# Test the function with known inputs
assert(incr_list([1, 2, 3]) == [2, 3, 4])
assert(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
```