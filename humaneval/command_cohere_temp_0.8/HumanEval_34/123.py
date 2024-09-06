```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. It does this by first converting the list into a set to remove any duplicate elements, and then converting it back to a list and sorting it before returning the modified list. 

This approach ensures that the resulting list contains only unique elements sorted in ascending order, as specified by the problem statement.