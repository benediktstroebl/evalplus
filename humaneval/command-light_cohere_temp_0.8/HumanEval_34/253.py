```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
l = ["a", "bb", "bb", "c", "d"]
assert unique(l) == ["a", "bb", "bb", "c", "d"]
```
The code defines a function `unique` that takes a list as input and returns a new list containing only the unique elements from the original list. It achieves this by first sorting the sorted order of all elements, and then using the set function to remove duplicates.