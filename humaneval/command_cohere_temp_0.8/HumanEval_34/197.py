```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This function leverages Python's powerful 'set' functionality and a list comprehension to efficiently filter out duplicate elements from the input list `l`. The 'set' data structure ensures that duplicate elements are automatically excluded during the iteration. The function then returns a sorted version of the resulting unique element list.

To follow the problem statement precisely, I've modified the function to sort the unique elements before returning the result. This adjustment ensures that the output is always a sorted list, providing consistent behavior regardless of the input list's original order.