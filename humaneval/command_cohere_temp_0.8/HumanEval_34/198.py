```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. The function uses the built-in `set` function to remove duplicate elements from the input list and then calls the `sort()` function to sort the unique elements. 

This solution passes the given test case, as shown in the following example:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

However, note that this code leaks memory when handling very large lists due to the inability to release the references held by the set, potentially causing significant performance issues. If the list is huge and this method is to be used, then the user should try using a different approach such as generating a list of tuple representations of the elements in the list and then comparing them using a `set` and `sort` method.