```python
def unique(lst):
    """Return sorted unique elements in a list"""
    unique = set(lst)
    return list(unique)

# Tests
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([1, 2, 3]) == [1, 2, 3]
assert unique([4, 7]) == [4, 7]
```  This code defines a `unique` function that returns a list of unique elements from the input list. It achieves this by converting the unique elements into a set and then back into a list.