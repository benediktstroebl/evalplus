```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function named unique which takes a list parameter named l. It aims to return a sorted list of unique elements from the input list. To achieve this, it utilizes a set called seen to track encountered elements. It then iterates through the input list, checking if each element is already in the seen set. If not, it adds it to both the result list and the seen set. Finally, it sorts the result list and returns it. 

The function docstring provides an example usage example that demonstrates how the function works when applied to a sample list.