```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function employs a set data structure named `seen` to keep track of unique elements. The list `l` is iterated over using a list comprehension, and for each element `x`, the condition `not (x in seen or seen.add(x))` is evaluated. If the element is not in the `seen` set, it is added to both the set and the `result` list. The final result is a sorted list containing all the unique elements from the input list.