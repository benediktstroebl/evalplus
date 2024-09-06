```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes a list l as an argument. It removes duplicate elements from the list using the set() function, which removes any duplicate values while maintaining the order of unique elements. Then, the sorted() function is applied to sort the elements alphabetically. Finally, it returns the sorted unique elements.