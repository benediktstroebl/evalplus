```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function called unique which takes a list l as input. It uses a set called seen to keep track of unique elements encountered while iterating through the input list. The function employs a list comprehension to filter out elements that are already in the seen set, effectively retaining only the unique elements. Lastly, the result list is sorted before being returned. The function achieves a O(nlog(n)) time complexity due to the sorting operation, which affords it the capability to efficiently handle lists with varying element ranges and counts.