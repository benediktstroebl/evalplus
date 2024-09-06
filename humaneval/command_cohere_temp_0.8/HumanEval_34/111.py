```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function called unique which takes a list l as input. It uses a set called seen to track unique elements. The function iterates through the input list, checking if each element x is already in the seen set. If not, it adds it to both the seen set and a result list. The function then returns the sorted result list, containing all the unique elements from the input list, sorted in ascending order.  It effectively delivers the functionality described in the problem statement.