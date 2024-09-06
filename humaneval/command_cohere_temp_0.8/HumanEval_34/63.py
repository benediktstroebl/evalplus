```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in Python set to automatically remove duplicate elements, and then sorts the remaining elements before returning the modified list.