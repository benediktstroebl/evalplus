```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function first converts the list into a set to remove duplicates, then converts the set back into a list and sorts it before returning the sorted unique list.

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This would output the following:
```
[0, 2, 3, 5, 9, 123]
``` 

This is an example of how the function can be used to remove duplicates from a list and sort the unique elements. 

The function unique can be used in a variety of cases, including handling duplicate entries in lists, filtering lists for specific use cases, and sorting unique elements for further analysis. 

Please let me know if I have addressed your requirement adequately, and if you have any additional questions or requirements!