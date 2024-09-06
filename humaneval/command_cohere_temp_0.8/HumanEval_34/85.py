```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted([item for item in l if not (item in seen or seen.add(item))])
```

This Python function uses a set, `seen`, to keep track of unique elements in the given list `l` while iterating through it. It adds elements to the set, neglecting duplicates, and subsequently sorts them before returning the resulting list. This method efficiently solves the problem while utilizing a straightforward approach to removing duplicates.