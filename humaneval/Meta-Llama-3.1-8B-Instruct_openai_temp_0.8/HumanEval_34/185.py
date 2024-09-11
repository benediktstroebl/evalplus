```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input and returns a sorted list of unique elements from `l`. It uses the built-in `set` data type to remove duplicates and the `sorted` function to sort the unique elements in ascending order.