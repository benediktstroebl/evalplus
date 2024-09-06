```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This approach utilizes a set `seen` to keep track of unique elements encountered while iterating through the list `l`. The generator expression `[x for x in l if not (x in seen or seen.add(x))]` efficiently checks if an element `x` is already in the `seen` set and adds it if it's not, resulting in a list of unique elements that are then sorted.  This solves the problem while maintaining a concise and efficient solution.