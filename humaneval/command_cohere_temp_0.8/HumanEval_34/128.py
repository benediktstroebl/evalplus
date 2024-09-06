```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This function leverages a set data structure to efficiently track and retrieve unique elements from the input list. It then returns the unique elements in a sorted order, as expected.