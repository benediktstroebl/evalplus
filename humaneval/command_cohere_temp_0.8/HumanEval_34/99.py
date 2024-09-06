```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list. The set `seen` keeps track of encountered elements, and the list `element` iterates over all elements in the input list `l`, checking if it has not been previously seen (`not in seen`) and adding it to the seen set (`and not seen.add(element)`). The elements are sorted as the list is constructed.