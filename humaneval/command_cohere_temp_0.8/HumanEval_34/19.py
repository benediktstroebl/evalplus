```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This approach utilizes a set, `seen`, to keep track of unique elements in the list `l` without repeated elements. The function returns a sorted list of these unique elements. 

Would you like to know more about any of the concepts used in this code? Let me know if I can help further refine this solution or provide additional insights.