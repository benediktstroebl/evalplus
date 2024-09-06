```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first converts the list into a set to remove duplicate elements, then converts the set back into a list and sorts it before returning the modified list.

Here is an example of how to use this function:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

The example usage demonstrates the function unique applied to the list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`. The function sorts and removes duplicate entries, returning the list `[0, 2, 3, 5, 9, 123]`, thus providing the unique elements in a sorted manner.