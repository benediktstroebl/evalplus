```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This code defines a function unique which takes a list l as input and returns a sorted list of unique elements from l. Within the function, a set seen is used to keep track of already-seen elements in the list. The function then employs a list comprehension to iterate through the input list, only adding elements to the output list if they have not already been added to the seen set. Lastly, the output list is sorted providing the function's result.