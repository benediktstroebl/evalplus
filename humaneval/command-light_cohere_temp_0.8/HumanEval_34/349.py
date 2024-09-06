```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([21, 23]) == [23]
assert unique([19, 19]) == [19]
assert unique([range(100)]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
```