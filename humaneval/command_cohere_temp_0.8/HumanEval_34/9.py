```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from l using the set method, which automatically eliminates duplicate values. Then, the sorted() method is applied to obtain a sorted list of unique elements, which is returned as the result. The function includes a docstring that describes its purpose and provides an example of its usage, which is useful for referencing when this solution is reused or needs to be updated in the future.