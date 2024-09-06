```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. The function uses the built-in `set` function to remove duplicate elements from the list, and then sorts the remaining unique elements before returning the result.