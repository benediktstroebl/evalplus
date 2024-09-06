```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called `unique` that takes a list `l` as an input. It uses the built-in `set` function to create a set from the input list, which automatically removes any duplicate elements. Then, it converts the set back to a list and sorts it using the `sort` function. Finally, it returns the sorted unique elements of the original list.