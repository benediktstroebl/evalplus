```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. The algorithm first removes duplicate elements using the `set()` function and then sorts the unique elements by using the `sort()` method. 

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) 
```

This will output the following:
```
[0, 2, 3, 5, 9, 123]
``` 

Which are the unique elements of the input list sorted into ascending order.