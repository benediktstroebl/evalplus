```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements present in l. The function first converts the list into a set to remove any duplicate elements, then converts it back to a list and sorts the unique elements in ascending order.