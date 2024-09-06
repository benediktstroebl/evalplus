```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first creates a set from the input list, which automatically removes any duplicate elements, then converts the set back to a list and sorts it before returning the result.