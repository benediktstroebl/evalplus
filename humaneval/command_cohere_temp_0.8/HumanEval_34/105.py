```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. The algorithm to solve this problem uses the following steps:
1. Convert the list to a set to remove duplicate elements.
2. Convert the set back to a list.
3. Sort the list.
4. Return the sorted list.

This approach efficiently solves the problem using built-in Python data structures and operations, resulting in a sorted list of unique elements.