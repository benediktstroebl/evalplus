```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes a list l as an argument. It removes duplicate elements from the list using the set method, which automatically eliminates duplicate values while maintaining the order of unique elements. Subsequently, the sorted() function is applied to sort the elements in ascending order. The function then returns the resulting list of unique and sorted elements.

Here is an example of how to use the unique function:
```python
my_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(my_list))
```

This would output the following:
```
[0, 2, 3, 5, 9, 123]
``` 

The result is a list containing only unique elements from the original my_list, arranged in ascending order.