```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements present in l. It removes duplicate elements using the set() function, which removes duplicate values by design in Python, and then sorts the unique elements using the sort() method.  This ensures that the resulting list contains only unique elements, and they are sorted in ascending order.  The function includes a docstring that describes its purpose and provides a usage example, which is convenient for developers to understand its functionality and usage hints.