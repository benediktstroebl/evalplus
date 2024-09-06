```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, l, which is a list. This function purges any duplicate elements within the list and subsequently sorts the unique elements in ascending order. The function concludes by returning the restructured list.

Here is an example usage of this function:
```python
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(result)
```

The output of this code is:
```bash
[0, 2, 3, 5, 9, 123]
``` 

This appropriately demonstrates the function's capability to sort and return unique elements from the input list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`.