```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. The algorithm first removes duplicate elements using the `set()` function and then sorts the unique elements by using the `sort()` method. 

Here is an example usage of the function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) 
```

The above code will output the following: 
 ```
[0, 2, 3, 5, 9, 123]
``` 

Which are the sorted unique elements in the input list. 

This function can be used to efficiently remove duplicate elements from a list and obtain a sorted unique element list.  It can be used anywhere sorting is required and is especially useful in scenarios such as storing unique items in a list, removing duplicate entries, and processing unique elements in a specific order. 

The implementation is self-contained, including a description of the function behavior in the docstring and a test example in the code comments. If you have any questions about the behavior of the function or how to use it, let me know!