```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This approach utilizes a set, `seen`, to keep track of unique elements in the list `l` without repeated elements. The function returns a sorted list of these unique elements. 

The docstring describes the function and provides an example use case. 

To handle a list of integers, like `[5, 3, 5, 2, 3, 3, 9, 0, 123]`, the function can be used as follows:
```python
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
``` 
The output will be:
```bash
[0, 2, 3, 5, 9, 123]
``` 
This list is sorted and contains only unique elements from the input list.