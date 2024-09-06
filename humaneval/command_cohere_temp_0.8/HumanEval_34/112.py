```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from l using the set method, which automatically eliminates duplicate values. Then, the sorted() function is used to sort the unique elements in ascending order. Finally, the sorted unique elements are returned as the output.