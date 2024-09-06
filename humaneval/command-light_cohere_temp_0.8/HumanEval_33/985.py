```python
def sort_third(lst):
    """Sorts list l such that all items not divisible by three are at the beginning."""
    lst[:] = [x for x in lst if x % 3 == 0]
    return [x for x in lst if x not in lst[:]] + lst[::]
# Test the function with a variety of inputs
assert all(sort_third([1, 2, 3]) == [1, 2, 3])
assert all(sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5])
assert all(sort_third([5, 6, 7, 8, 9]) == [5, 6, 8, 9])
assert all(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
```