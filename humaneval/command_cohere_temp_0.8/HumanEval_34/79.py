```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. Elements that are not already in the set are added to the result list, which ensures only unique elements are included. Finally, the result is sorted to provide a consistent order of unique elements.