```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list comprehension to efficiently filter out duplicate elements. The set `seen` keeps track of elements encountered, and the list comprehension `element for element in l if element not in seen and not seen.add(element)` iterates over the list `l`, checking if elements are already in the `seen` set and adding them to the resulting list if they are not. The returned list is then sorted using the `sorted` function.