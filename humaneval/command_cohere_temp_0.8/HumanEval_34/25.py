```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from l using the set() function, which removes duplicate values and converts the list into a set. Then, the function sorts the unique elements using the sort() method and returns the sorted unique list.