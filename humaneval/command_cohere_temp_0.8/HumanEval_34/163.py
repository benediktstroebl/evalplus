```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function called unique which takes a list l as input. It uses a set called seen to keep track of unique elements encountered while iterating through the input list. The function filters elements from the input list using a list comprehension, excluding elements that are already in the seen set. The resulting unique elements are stored in the result list. Finally, the function returns the sorted result list ensuring that the unique elements are sorted in ascending order. 

The function docstring provides an example usage scenario, where it is tested with a sample list and its corresponding output.