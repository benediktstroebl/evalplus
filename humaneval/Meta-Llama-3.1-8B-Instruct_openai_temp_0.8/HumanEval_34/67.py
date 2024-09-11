```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines the `unique` function which uses Python's built-in `set` function to remove duplicates from the list, then sorts the resulting unique elements with the `sorted` function. 

When you run this script, it will print the sorted list of unique elements: `[0, 2, 3, 5, 9, 123]`