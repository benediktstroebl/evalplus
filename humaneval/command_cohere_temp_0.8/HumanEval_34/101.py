```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. This function uses the `set()` function to convert the list into a set, eliminating duplicate elements, and finally converts it back to a list and sorts it using the `sort()` method. 

This solution corresponds to the problem statement and passes the given tests. Feel free to ask for further clarification or provide additional details for more tailored assistance.