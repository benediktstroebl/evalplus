```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function named unique which takes a list l as input. Inside the function, a set called seen is used to keep track of unique elements encountered while iterating through the input list. The function uses a list comprehension to select only the elements that have not already been seen or added to the seen set, these are then added to the seen set and considered as unique. Finally, the function returns the sorted unique elements. The function provides a description of its purpose in the docstring, which is helpful for understanding its behavior.