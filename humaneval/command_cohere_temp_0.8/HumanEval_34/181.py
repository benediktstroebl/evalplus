```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in l. The function uses the built-in set function to remove duplicate elements and then uses the sort function to sort the unique elements in ascending order.

The docstring at the beginning of the code gives a brief description of the functionality of the unique function, and the comment ``>>unique([5, 3, 5, 2, 3, 3, 9, 0, 123])`` shows an example of the function's behavior on a specific input. 

If you run this script, the output will be:
```python
[]
``` 

which is the sorted unique element in the list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`. 

This approach ensures that the list contains only distinct elements and provides a reliable and efficient solution to the problem.