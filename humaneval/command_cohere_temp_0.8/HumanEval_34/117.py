```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. The function uses the built-in Python set data structure, which automatically removes any duplicate elements while ensuring that the order of elements remains unchanged. Subsequently, the function sorts the resulting unique list before returning the sorted list of distinct elements.