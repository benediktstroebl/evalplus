```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements present in l. The function first removes any duplicate elements from l using the set method, which automatically eliminates duplicate values. Then, the list is sorted in ascending order using the sort method. Ultimately, the function returns the sorted unique list. The function comment denotes the problem that the code is solving: returning a sorted list of distinct values in a given list.