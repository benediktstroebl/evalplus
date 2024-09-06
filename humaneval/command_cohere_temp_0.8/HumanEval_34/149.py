```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The above method uses a set called 'seen' to keep track of unique elements encountered while iterating over the list 'l'. Elements that are not already in the set are added to the result list, which is then sorted.  This ensures that the output is a list of sorted unique elements from the input list.  This approach uses a set data structure to efficiently track and retrieve unique elements, resulting in an optimized solution.