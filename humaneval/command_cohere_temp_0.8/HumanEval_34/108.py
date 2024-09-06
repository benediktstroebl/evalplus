```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first removes duplicate elements from the list using the set() function, which removes duplicate values and converts the list to a set. Then, the function sorts the unique elements using the sort() method and returns the sorted unique list.

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

The output of this code will be:
```
[0, 2, 3, 5, 9, 123]
```

The function unique() can be called with the list [[5, 3, 5, 2, 3, 3, 9, 0, 123]] and it will return the sorted unique elements in the list, which are [0, 2, 3, 5, 9, 123] in this case.