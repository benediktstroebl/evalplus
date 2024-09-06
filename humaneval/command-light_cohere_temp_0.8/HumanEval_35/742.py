```python
def max_element(lst):
    return lst[0] if lst and len(lst) else None

# Test cases
max_elems = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert max_elems == 123

max_elems = max_element([1, 2, 3])
assert max_elems == 3

max_elems = max_element([5, 2, 3, -5, -2, -3, -1])
assert max_elems == 3

max_elems = max_element([1, 2, 3, 4, 5, 6])
assert max_elems is None
```