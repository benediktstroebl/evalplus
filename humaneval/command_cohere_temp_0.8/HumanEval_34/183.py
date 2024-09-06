```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list. The set `seen` keeps track of encountered elements, and the list `element` iterates over elements in the input list `l`. The sorting step is carried out using the `sorted` function to ensure consistent output.