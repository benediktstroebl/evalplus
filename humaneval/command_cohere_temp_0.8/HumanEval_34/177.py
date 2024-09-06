```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes a list l as an argument. It removes duplicate elements from the list using the set method, which automatically eliminates duplicate values by assigning them to keys in a dictionary (keys are the elements, values are ignored). The function then sorts the unique elements alphabetically and returns the newly modified list.

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This will output:
```
[0, 2, 3, 5, 9, 123]
```

which is the sorted list of unique elements of the input list.