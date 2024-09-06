```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function called unique which takes a list l as input. It uses a set called seen to keep track of unique elements encountered while iterating through the input list. The function filters elements from the input list using a list comprehension, excluding elements that are already in the seen set. This ensures that only unique elements are included. Finally, the function returns a sorted version of the result list containing the unique elements in sorted order.