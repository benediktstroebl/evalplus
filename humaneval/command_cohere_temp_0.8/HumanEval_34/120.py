```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list comprehension to efficiently solve the problem. The set `seen` keeps track of encountered elements, and the list comprehension 'element for element in l if ...' is used to both filter elements that haven't been seen and ensure elements get added to the set. Overall, this provides an optimized solution to the problem.