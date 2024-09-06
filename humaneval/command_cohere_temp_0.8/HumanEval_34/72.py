```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function unique takes a list l as input and returns a sorted list of unique elements. To do this, it utilizes a set seen to track elements already encountered. The list comprehension filters out elements in l that are already in the seen set or have been newly added to it. The result list is then sorted, and returned as the solution.