```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements. It removes duplicate elements from the list using the `set()` function, which automatically filters out duplicates, and then sorts the unique elements using the `sort()` function. 

The function is designed to provide a concise and efficient way to obtain a sorted list of distinct elements from an input list.