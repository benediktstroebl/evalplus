```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from the list using the set method, which automatically eliminates duplicate values. Then, the sorted() method is used to sort the unique elements in ascending order. 

The docstring at the beginning of the code describes the function's purpose and provides an example of how the function can be used. The example list is [5, 3, 5, 2, 3, 3, 9, 0, 123], and the function's output is [0, 2, 3, 5, 9, 123]. This demonstrates how the unique function can be used to efficiently remove duplicate elements from a list and sort the remaining unique elements.