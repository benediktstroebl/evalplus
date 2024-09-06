```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in the input list. The function first removes duplicate elements from the list using the set method, which automatically eliminates duplicate values, and then sorts the unique elements using the sort method. 

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This will output:
```
[0, 2, 3, 5, 9, 123]
```
as expected.