```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting the list to a set, and then returns the elements in sorted order. The test at the end shows that the function works as expected. 

This script will output:
```
[0, 2, 3, 5, 9, 123]
```