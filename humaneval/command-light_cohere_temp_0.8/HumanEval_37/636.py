```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [0] * len(lst) - 1] + lst[-1:]

# Test cases
test_sort_even = [
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 20, 30]) == [10, 20, 30]
]
```