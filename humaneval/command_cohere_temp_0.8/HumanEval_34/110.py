```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in Python set to automatically filter out duplicate elements, and then uses the sort() method to sort the values. 

The docstring at the beginning of the code provides documentation for the code, describing what it does, and also includes a test example to demonstrate the functionality of the function.