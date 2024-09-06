```python
def sort_even(lst):
    """Sorts an even list in-C."""
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Test cases for function sort_even
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
assert sort_even([11, 22, 33]) == [11, 22, 33]
```